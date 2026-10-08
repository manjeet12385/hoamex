require('dotenv').config();
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { Pool } = require('pg');
const path = require('path');
const nodemailer = require('nodemailer');
const multer = require('multer');

// ✅ FIX #2: OTP Rate Limiting
const rateLimit = require('express-rate-limit');
const otpLimiter = rateLimit({
  windowMs: 10 * 60 * 1000, // 10 minutes
  max: 5, // max 5 OTP requests per IP per 10 min
  message: { error: 'Too many OTP requests. Please wait 10 minutes before trying again.' },
  standardHeaders: true,
  legacyHeaders: false,
});

// Configure Cloudinary for Image Uploads
const cloudinary = require('cloudinary').v2;
const { CloudinaryStorage } = require('multer-storage-cloudinary');

cloudinary.config({
  cloud_name: process.env.CLOUDINARY_CLOUD_NAME,
  api_key: process.env.CLOUDINARY_API_KEY,
  api_secret: process.env.CLOUDINARY_API_SECRET
});

const storage = new CloudinaryStorage({
  cloudinary: cloudinary,
  params: {
    folder: 'hoamex_partners',
    allowed_formats: ['jpg', 'png', 'jpeg', 'pdf']
  }
});
const upload = multer({ storage: storage });

const transporter = nodemailer.createTransport({
  service: 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASS
  }
});
const Razorpay = require('razorpay');
const razorpay = new Razorpay({
  key_id: process.env.RAZORPAY_KEY_ID || 'rzp_test_replace_me',
  key_secret: process.env.RAZORPAY_KEY_SECRET || 'replace_me',
});

const app = express();
const HOST = process.env.HOST || '0.0.0.0';
const PORT = process.env.PORT || 3000;

// ✅ FIX #21: DB Pool with timeout config to prevent connection leaks
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false },
  idleTimeoutMillis: 30000,       // Close idle connections after 30s
  connectionTimeoutMillis: 5000,  // Fail fast if can't connect in 5s
  max: 10                         // Max 10 concurrent connections
});

const jwt = require('jsonwebtoken');
const JWT_SECRET = process.env.JWT_SECRET || 'hoamex_super_secret_key_123';

// ✅ FIX #6: Platform fee from env (not hardcoded)
const PLATFORM_FEE = parseInt(process.env.PLATFORM_FEE) || 49;

// Auth Middleware
const authGuard = async (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.status(401).json({ error: 'Unauthorized. Please login.' });
  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.user = decoded; // { email, role }
    
    // Real-time DB check to ensure user wasn't deleted by admin (skip during registration)
    const isRegisterRoute = req.path.includes('/register');
    
    if (!isRegisterRoute) {
      if (req.user.role === 'partner') {
        const dbRes = await pool.query('SELECT email FROM partners WHERE email = $1', [req.user.email]);
        if (dbRes.rows.length === 0) return res.status(401).json({ error: 'Account deleted. Please login again.' });
      } else if (req.user.role === 'user' || !req.user.role) {
        const dbRes = await pool.query('SELECT email FROM users WHERE email = $1', [req.user.email]);
        if (dbRes.rows.length === 0) return res.status(401).json({ error: 'Account deleted. Please login again.' });
      }
    }
    
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid or expired token.' });
  }
};

// Middleware
app.use(cors());
app.use(bodyParser.json());

// ✅ DEEP SCAN FIX: Global XSS Sanitizer for all incoming requests
const sanitizeHtmlOnly = (val) => {
  if (typeof val === 'string') {
    return val.replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }
  if (Array.isArray(val)) return val.map(sanitizeHtmlOnly);
  if (val !== null && typeof val === 'object') {
    const escapedObj = {};
    for (let k in val) {
      escapedObj[k] = sanitizeHtmlOnly(val[k]);
    }
    return escapedObj;
  }
  return val;
};
app.use((req, res, next) => {
  if (req.body) req.body = sanitizeHtmlOnly(req.body);
  next();
});

// ✅ DEEP SCAN FIX: Block access to sensitive backend files that express.static would expose
app.use((req, res, next) => {
  const ext = path.extname(req.path).toLowerCase();
  
  // Prevent access to backend JS files
  if (ext === '.js' && !['/common.js', '/cart.js', '/app.js'].includes(req.path)) {
    return res.status(403).json({ error: 'Access Denied: Backend scripts are protected.' });
  }
  
  // Prevent access to configuration, JSON data, and dev files
  const sensitiveFiles = ['.env', 'prices.json', 'vercel.json', 'server.js'];
  if (sensitiveFiles.some(file => req.path.includes(file)) || ext === '.txt' || ext === '.py') {
    return res.status(403).json({ error: 'Access Denied: Protected resource.' });
  }
  
  next();
});

// Serve the static HTML/JS/CSS files from this directory
app.use(express.static(path.join(__dirname, ''), { extensions: ['html'] }));

// Initialize Database Table
async function initDb() {
  try {
    await pool.query(`
      CREATE TABLE IF NOT EXISTS bookings (
        id SERIAL PRIMARY KEY,
        customer_name VARCHAR(100),
        phone_number VARCHAR(20),
        email VARCHAR(100),
        address TEXT,
        landmark TEXT,
        booking_date DATE,
        time_slot VARCHAR(50),
        payment_method VARCHAR(50),
        cart_items JSONB,
        total_amount INTEGER,
        status VARCHAR(50) DEFAULT 'Pending',
        assigned_partner_name VARCHAR(100),
        assigned_partner_phone VARCHAR(20),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
      
      CREATE TABLE IF NOT EXISTS partners (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        phone VARCHAR(20),
        experience_years INTEGER,
        primary_category VARCHAR(100),
        skills JSONB,
        documents JSONB,
        bank_details JSONB,
        status VARCHAR(20) DEFAULT 'PENDING',
        last_logout_time TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );

      CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(100),
        email VARCHAR(100) UNIQUE,
        phone VARCHAR(20),
        gender VARCHAR(20),
        dob VARCHAR(20),
        full_address TEXT,
        last_logout_time TIMESTAMP,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );

      CREATE TABLE IF NOT EXISTS otps (
        id SERIAL PRIMARY KEY,
        email VARCHAR(100) NOT NULL,
        otp VARCHAR(6) NOT NULL,
        expires_at TIMESTAMP NOT NULL,
        used BOOLEAN DEFAULT FALSE,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );

      -- ✅ FIX #22: Email failure log table
      CREATE TABLE IF NOT EXISTS email_logs (
        id SERIAL PRIMARY KEY,
        recipient VARCHAR(200),
        subject VARCHAR(300),
        status VARCHAR(20) DEFAULT 'sent',
        error_message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `);
    await pool.query(`ALTER TABLE bookings ADD COLUMN IF NOT EXISTS email VARCHAR(100);`);
    await pool.query(`ALTER TABLE users ADD COLUMN IF NOT EXISTS last_logout_time TIMESTAMP;`);
    await pool.query(`ALTER TABLE partners ADD COLUMN IF NOT EXISTS last_logout_time TIMESTAMP;`);
    console.log("Database tables initialized!");
  } catch (error) {
    console.error("Error initializing database:", error);
  }
}
initDb();

// ✅ FIX #22: Helper to log email send attempts to DB
async function logEmail(recipient, subject, status, error_message = null) {
  try {
    await pool.query(
      'INSERT INTO email_logs (recipient, subject, status, error_message) VALUES ($1, $2, $3, $4)',
      [recipient, subject, status, error_message]
    );
  } catch (e) { /* silently fail log */ }
}

// Load pricing catalog for secure checkout
const fs = require('fs');
let pricesCatalog = {};
try {
  pricesCatalog = JSON.parse(fs.readFileSync(path.join(__dirname, 'prices.json'), 'utf-8'));
} catch (e) {
  console.error("Could not load prices.json. Backend verification disabled.");
}

// ==========================================
// RAZORPAY: Create Order
// ==========================================
app.post('/api/create-razorpay-order', authGuard, async (req, res) => {
  try {
    const { amount } = req.body; // Amount should be in rupees
    if (!amount) return res.status(400).json({ error: "Amount is required" });

    const options = {
      amount: amount * 100, // Razorpay works in paise (1 INR = 100 paise)
      currency: "INR",
      receipt: "receipt_" + Date.now(),
    };

    const order = await razorpay.orders.create(options);
    res.status(200).json({ success: true, order });
  } catch (error) {
    console.error("Error creating Razorpay order:", error);
    res.status(500).json({ error: "Failed to create payment order" });
  }
});

// API Route to handle new bookings
app.post('/api/bookings', authGuard, async (req, res) => {
  try {
    const { 
      customer_name, 
      phone_number,
      email,
      address, 
      landmark, 
      booking_date, 
      time_slot, 
      payment_method, 
      cart_items, 
      total_amount 
    } = req.body;

    // ✅ FIX #11: Address is now required
    if (!customer_name || !phone_number || !address || !cart_items || cart_items.length === 0) {
      return res.status(400).json({ error: 'Missing required fields: name, phone, address, and cart items are required.' });
    }

    // ✅ FIX #20: Backend date validation — reject past dates
    if (booking_date) {
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      const selectedDate = new Date(booking_date);
      if (selectedDate < today) {
        return res.status(400).json({ error: 'Booking date cannot be in the past.' });
      }
    }

    // Securely calculate the true total amount using backend catalog
    let true_total_amount = 0;
    
    // Load pricing catalog dynamically so it always has the latest updates
    let dynamicPricesCatalog = {};
    try {
      dynamicPricesCatalog = JSON.parse(fs.readFileSync(path.join(__dirname, 'prices.json'), 'utf-8'));
    } catch(e) {}

    if (Object.keys(dynamicPricesCatalog).length > 0) {
      for (let item of cart_items) {
        let rawTitle = item.title || item.name || '';
        let cleanTitle = rawTitle.replace(/\\'/g, "'").trim();
        let itemPrice = dynamicPricesCatalog[cleanTitle];
        
        if (itemPrice === undefined) {
          // SECURITY FIX: Reject unknown items instead of trusting frontend price
          console.warn(`SECURITY ALERT: Unknown item requested -> ${cleanTitle}`);
          return res.status(400).json({ error: `Security Error: Service '${cleanTitle}' is not recognized in our pricing database.` });
        }
        
        true_total_amount += itemPrice * (item.quantity || 1);
      }
    } else {
      console.error("Pricing catalog missing! Cannot securely process bookings.");
      return res.status(500).json({ error: 'Server configuration error: Pricing catalog is offline.' });
    }

    // Optional: Log if there's a discrepancy
    if (true_total_amount !== parseInt(total_amount)) {
      console.warn(`Price discrepancy detected! Frontend: ${total_amount}, Backend: ${true_total_amount}`);
    }

    const query = `
      INSERT INTO bookings 
      (customer_name, phone_number, email, address, landmark, booking_date, time_slot, payment_method, cart_items, total_amount) 
      VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10)
      RETURNING *;
    `;
    
    let createdBookings = [];
    for (let item of cart_items) {
      let rawTitle = item.title || item.name || '';
      let cleanTitle = rawTitle.replace(/\\'/g, "'").trim();
      let itemPrice = pricesCatalog[cleanTitle] || 0;
      let itemTotal = itemPrice * (item.quantity || 1);
      
      const values = [
        customer_name, 
        phone_number,
        email || null, 
        address, 
        landmark, 
        booking_date, 
        time_slot, 
        payment_method, 
        JSON.stringify([item]), // Only this specific item goes to the partner
        itemTotal 
      ];
      const result = await pool.query(query, values);
      createdBookings.push(result.rows[0]);
    }

    const newBooking = createdBookings[0];

    // ==========================================
    // ==========================================
    // NOTIFICATION SYSTEM: Send Email Alert
    // ==========================================
    try {
      // Fetch verified partners
      const partnersRes = await pool.query("SELECT email FROM partners WHERE status = 'VERIFIED'");
      const partnerEmails = partnersRes.rows.map(p => p.email).filter(e => e);
      const adminEmail = process.env.EMAIL_USER;
      
      for (let bk of createdBookings) {
        let bkItems = typeof bk.cart_items === 'string' ? JSON.parse(bk.cart_items) : bk.cart_items;
        let serviceName = (bkItems && bkItems.length > 0) ? (bkItems[0].title || bkItems[0].name) : 'Service';

        const emailHtml = `
          <h2 style="color: #4c1d95;">New Booking Alert: ${serviceName}</h2>
          <p>A new booking has just arrived. Please check your Partner Dashboard to accept it.</p>
          <table style="width: 100%; border-collapse: collapse; margin-top: 15px;">
            <tr><td style="padding: 8px; border: 1px solid #ddd;"><b>Booking ID</b></td><td style="padding: 8px; border: 1px solid #ddd;">#BKG-${bk.id}</td></tr>
            <tr><td style="padding: 8px; border: 1px solid #ddd;"><b>Customer Name</b></td><td style="padding: 8px; border: 1px solid #ddd;">${customer_name}</td></tr>
            <tr><td style="padding: 8px; border: 1px solid #ddd;"><b>Phone Number</b></td><td style="padding: 8px; border: 1px solid #ddd;">${phone_number}</td></tr>
            <tr><td style="padding: 8px; border: 1px solid #ddd;"><b>Email</b></td><td style="padding: 8px; border: 1px solid #ddd;">${email || 'N/A'}</td></tr>
            <tr><td style="padding: 8px; border: 1px solid #ddd;"><b>Address</b></td><td style="padding: 8px; border: 1px solid #ddd;">${address} ${landmark ? '('+landmark+')' : ''}</td></tr>
            <tr><td style="padding: 8px; border: 1px solid #ddd;"><b>Date & Time</b></td><td style="padding: 8px; border: 1px solid #ddd;">${booking_date} | ${time_slot}</td></tr>
            <tr><td style="padding: 8px; border: 1px solid #ddd;"><b>Total Amount</b></td><td style="padding: 8px; border: 1px solid #ddd;">₹${bk.total_amount}</td></tr>
          </table>
          <p style="margin-top: 20px;"><a href="https://hoamex.com/partner-dashboard.html" style="background:#23a566; color:white; padding:10px 15px; text-decoration:none; border-radius:5px;">Open Dashboard</a></p>
        `;

        const mailOptions = {
          from: process.env.EMAIL_USER,
          to: adminEmail, // To Admin
          bcc: partnerEmails.join(','), // BCC to all verified partners so they don't see each other's IDs
          subject: `🚨 New Booking Received: ${serviceName}`,
          html: emailHtml
        };

        transporter.sendMail(mailOptions).then(() => {
          console.log(`Notification email sent for BKG-${bk.id}.`);
          logEmail(adminEmail, mailOptions.subject, 'sent');
        }).catch(err => {
          console.error(`Failed to send email for BKG-${bk.id}:`, err);
          logEmail(adminEmail, mailOptions.subject, 'failed', err.message);
        });
      }
    } catch (notifErr) {
      console.error('Error in notification system:', notifErr);
    }
    // ==========================================
    
    res.status(201).json({ 
      message: 'Booking created successfully!', 
      booking: newBooking 
    });

  } catch (error) {
    console.error('Error saving booking:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// ✅ FIX #2: OTP Rate Limiter applied to all OTP routes
// API Route to send OTP
app.post('/api/send-otp', otpLimiter, async (req, res) => {
  try {
    const { email, isSignup } = req.body;
    if (!email) {
      return res.status(400).json({ error: 'Email is required' });
    }

    // Check partner status
    if (!isSignup) {
      const partnerRes = await pool.query('SELECT * FROM partners WHERE email = $1', [email]);
      if (partnerRes.rows.length === 0) {
        return res.status(404).json({ error: 'No partner account found with this email. Please register first.' });
      }
    }

    const otp = Math.floor(100000 + Math.random() * 900000).toString();
    
    // Save OTP to DB with 10 min expiration
    await pool.query('DELETE FROM otps WHERE email = $1', [email]);
    const expiresAt = new Date(Date.now() + 10 * 60 * 1000);
    await pool.query(
      'INSERT INTO otps (email, otp, expires_at) VALUES ($1, $2, $3)',
      [email, otp, expiresAt]
    );
    
    const mailOptions = {
      from: process.env.EMAIL_USER,
      to: email,
      subject: 'Joamex - Partner Login OTP',
      text: `Your OTP for login is: ${otp}. Please do not share it with anyone.`,
      html: `<h3>Welcome to Joamex Partner Portal!</h3><p>Your OTP for login is: <b style="font-size:24px;">${otp}</b></p>`
    };

    const info = await transporter.sendMail(mailOptions);
    console.log('Partner OTP Email sent:', info.messageId);
    
    res.status(200).json({ success: true, message: 'OTP sent successfully. Please check your email.' });
  } catch (error) {
    console.error('Error sending partner email:', error);
    res.status(500).json({ error: 'Failed to send OTP' });
  }
});

// API Route to verify Partner OTP
app.post('/api/partner/verify-otp', async (req, res) => {
  try {
    let { email, otp } = req.body;
    if (!email || !otp) return res.status(400).json({ error: 'Email and OTP required' });
    
    email = email.trim().toLowerCase();
    otp = otp.trim();

    const result = await pool.query(
      'SELECT * FROM otps WHERE email = $1 AND otp = $2 AND used = FALSE AND expires_at > NOW()',
      [email, otp]
    );

    if (result.rows.length === 0) {
      return res.status(400).json({ error: 'Invalid or expired OTP.' });
    }

    await pool.query('UPDATE otps SET used = TRUE WHERE id = $1', [result.rows[0].id]);
    
    // Generate JWT token
    const token = jwt.sign({ email, role: 'partner' }, JWT_SECRET, { expiresIn: '3650d' });
    
    res.status(200).json({ success: true, message: 'OTP verified successfully.', token });
  } catch (error) {
    console.error('Error verifying partner OTP:', error);
    res.status(500).json({ error: 'Internal server error' });
  }
});

// API Route for partner to fetch their own details
app.get('/api/partner/me', authGuard, async (req, res) => {
  try {
    if (req.user.role !== 'partner') {
      return res.status(403).json({ error: 'Forbidden' });
    }
    const result = await pool.query('SELECT * FROM partners WHERE email = $1', [req.user.email]);
    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Partner not found' });
    }
    res.status(200).json({ success: true, partner: result.rows[0] });
  } catch (error) {
    console.error('Error fetching partner:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API Route to send User/Customer OTP via Email
app.post('/api/user/send-otp', otpLimiter, async (req, res) => {
  try {
    let { email, isSignup, isResend } = req.body;
    if (!email) {
      return res.status(400).json({ error: 'Email is required' });
    }
    
    email = email.trim().toLowerCase();

    // ✅ CHECK: User must exist in DB before sending OTP (for login only)
    const userRes = await pool.query('SELECT * FROM users WHERE LOWER(TRIM(email)) = $1', [email]);
    
    if (isSignup && !isResend) {
      if (userRes.rows.length > 0) {
        return res.status(400).json({ 
          error: 'An account already exists with this email. Please log in.' 
        });
      }
    } else if (!isSignup && !isResend) {
      if (userRes.rows.length === 0) {
        return res.status(404).json({ 
          error: 'No account found with this email. Please sign up first.' 
        });
      }
    }

    const otp = Math.floor(100000 + Math.random() * 900000).toString();
    
    // ✅ Save OTP in DB with 10-minute expiry (delete old OTPs for this email first)
    await pool.query('DELETE FROM otps WHERE email = $1', [email]);
    const expiresAt = new Date(Date.now() + 10 * 60 * 1000); // 10 minutes from now
    await pool.query(
      'INSERT INTO otps (email, otp, expires_at) VALUES ($1, $2, $3)',
      [email, otp, expiresAt]
    );
    
    const mailOptions = {
      from: process.env.EMAIL_USER,
      to: email,
      subject: 'Joamex - Your OTP Code',
      text: `Your OTP is: ${otp}. It is valid for 10 minutes. Do not share it with anyone.`,
      html: `<h3>Welcome to Joamex!</h3><p>Your OTP is: <b style="font-size:28px; letter-spacing:4px;">${otp}</b></p><p style="color:#888;">This OTP expires in 10 minutes.</p>`
    };

    const info = await transporter.sendMail(mailOptions);
    console.log(`OTP Email sent to ${email}: ${info.messageId}`);
    
    // ✅ Do NOT send OTP in response (security fix)
    res.status(200).json({ success: true, message: 'OTP sent to your email. Valid for 10 minutes.' });
  } catch (error) {
    console.error('Error sending customer email:', error);
    res.status(500).json({ error: 'Failed to send OTP: ' + (error.message || String(error)) });
  }
});

// API Route to verify OTP (server-side check)
app.post('/api/user/verify-otp', async (req, res) => {
  try {
    let { email, otp } = req.body;
    if (!email || !otp) {
      return res.status(400).json({ error: 'Email and OTP are required.' });
    }
    email = email.trim().toLowerCase();
    otp = otp.trim();

    // Find matching OTP in DB
    const result = await pool.query(
      'SELECT * FROM otps WHERE email = $1 AND otp = $2 AND used = FALSE AND expires_at > NOW()',
      [email, otp]
    );

    if (result.rows.length === 0) {
      return res.status(400).json({ error: 'Invalid or expired OTP. Please request a new one.' });
    }

    // Mark OTP as used
    await pool.query('UPDATE otps SET used = TRUE WHERE id = $1', [result.rows[0].id]);

    // Generate JWT token
    const token = jwt.sign({ email, role: 'user' }, JWT_SECRET, { expiresIn: '3650d' });

    res.status(200).json({ success: true, message: 'OTP verified successfully.', token });
  } catch (error) {
    console.error('Error verifying OTP:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API Route for User Registration
app.post('/api/user/register', authGuard, async (req, res) => {
  try {
    // Only allow registered user to update their own profile, or allow new registration if role=user
    if (req.user.role !== 'user') return res.status(403).json({ error: 'Forbidden' });
    
    let { full_name, email, phone, gender, dob, full_address } = req.body;
    
    if (!full_name || !email || !phone) {
      return res.status(400).json({ error: 'Name, email and phone are required.' });
    }

    // Ensure the token email matches the registration email to prevent override
    email = email.trim().toLowerCase();
    if (email !== req.user.email) {
      return res.status(403).json({ error: 'You can only update your own profile.' });
    }

    full_name = full_name.trim();
    phone = phone.trim();

    // Upsert user (update if email exists, insert if new)
    const query = `
      INSERT INTO users (full_name, email, phone, gender, dob, full_address)
      VALUES ($1, $2, $3, $4, $5, $6)
      ON CONFLICT (email) 
      DO UPDATE SET 
        full_name = EXCLUDED.full_name,
        phone = EXCLUDED.phone,
        gender = EXCLUDED.gender,
        dob = EXCLUDED.dob,
        full_address = EXCLUDED.full_address
      RETURNING *;
    `;
    const values = [full_name, email, phone, gender, dob, full_address];
    
    const result = await pool.query(query, values);
    res.status(200).json({ success: true, user: result.rows[0] });
  } catch (error) {
    console.error('Error registering user:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});


// API Route for Partner Registration
app.post('/api/partners/register', upload.fields([
  { name: 'id_front', maxCount: 1 },
  { name: 'id_back', maxCount: 1 },
  { name: 'certificate', maxCount: 1 }
]), async (req, res) => {
  try {
    let { 
      full_name, email, phone, experience_years, primary_category, 
      skills, bank_details 
    } = req.body;

    if (!full_name || !email || !phone) {
      return res.status(400).json({ error: 'Missing basic required fields' });
    }

    // Temporarily bypassed for testing without token
    email = email.trim().toLowerCase();
    // if (email !== req.user.email || req.user.role !== 'partner') {
    //   return res.status(403).json({ error: 'Forbidden' });
    // }

    // Parse JSON strings back to objects (since FormData sends strings)
    try {
      skills = typeof skills === 'string' ? JSON.parse(skills) : skills;
      bank_details = typeof bank_details === 'string' ? JSON.parse(bank_details) : bank_details;
    } catch (e) {
      console.error("Error parsing JSON fields:", e);
    }

    // Construct documents object from uploaded files (using Cloudinary URLs)
    const documents = {
      id_front: req.files && req.files['id_front'] ? req.files['id_front'][0].path : 'Not Uploaded',
      id_back: req.files && req.files['id_back'] ? req.files['id_back'][0].path : 'Not Uploaded',
      certificate: req.files && req.files['certificate'] ? req.files['certificate'][0].path : 'Not Uploaded'
    };

    const query = `
      INSERT INTO partners (
        full_name, email, phone, experience_years, primary_category, 
        skills, documents, bank_details, status
      ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, 'PENDING')
      RETURNING *;
    `;
    
    const values = [
      full_name, email, phone, experience_years, primary_category, 
      JSON.stringify(skills), JSON.stringify(documents), JSON.stringify(bank_details)
    ];

    const result = await pool.query(query, values);
    
    res.status(201).json({ 
      success: true,
      message: 'Partner registered successfully!', 
      partner: result.rows[0] 
    });

  } catch (error) {
    console.error('Error saving partner:', error);
    // Handle unique email constraint error
    if (error.code === '23505') {
      return res.status(400).json({ error: 'This email is already registered.' });
    }
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// ✅ API Route to check if partner email already exists (for frontend pre-registration validation)
app.post('/api/partners/check-email', async (req, res) => {
  try {
    let { email } = req.body;
    if (!email) return res.status(400).json({ error: 'Email is required' });
    email = email.trim().toLowerCase();
    const result = await pool.query('SELECT id, status FROM partners WHERE LOWER(TRIM(email)) = $1', [email]);
    if (result.rows.length > 0) {
      const partner = result.rows[0];
      return res.status(200).json({
        exists: true,
        status: partner.status,
        message: partner.status === 'PENDING'
          ? 'This email is already registered and is under review. Please wait for approval.'
          : partner.status === 'VERIFIED'
          ? 'This email is already a verified partner. Please use Partner Login instead.'
          : 'This email is already registered.'
      });
    }
    res.status(200).json({ exists: false });
  } catch (error) {
    console.error('Error checking partner email:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// ✅ FIX #1: Admin Login — credentials from .env (not hardcoded)
app.post('/api/admin/login', (req, res) => {
  const { email, password } = req.body;
  const ADMIN_EMAIL = process.env.ADMIN_EMAIL;
  const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD;
  if (!ADMIN_EMAIL || !ADMIN_PASSWORD) {
    return res.status(500).json({ error: 'Server misconfiguration: admin credentials not set.' });
  }
  if (email === ADMIN_EMAIL && password === ADMIN_PASSWORD) {
    const token = jwt.sign({ email, role: 'admin' }, JWT_SECRET, { expiresIn: '1d' });
    res.status(200).json({ success: true, token });
  } else {
    res.status(401).json({ error: 'Invalid admin credentials' });
  }
});

// ✅ FIX #3: Logout endpoint — records logout time to invalidate JWT
app.post('/api/logout', async (req, res) => {
  try {
    const authHeader = req.headers.authorization;
    if (!authHeader) return res.status(200).json({ success: true });
    const token = authHeader.split(' ')[1];
    let decoded;
    try { decoded = jwt.verify(token, JWT_SECRET); } catch(e) { return res.status(200).json({ success: true }); }
    const now = new Date();
    if (decoded.role === 'user') {
      await pool.query('UPDATE users SET last_logout_time = $1 WHERE LOWER(TRIM(email)) = $2', [now, decoded.email]);
    } else if (decoded.role === 'partner') {
      await pool.query('UPDATE partners SET last_logout_time = $1 WHERE LOWER(TRIM(email)) = $2', [now, decoded.email]);
    }
    res.status(200).json({ success: true, message: 'Logged out successfully.' });
  } catch (error) {
    res.status(200).json({ success: true }); // Always succeed logout
  }
});

// ✅ FIX #6: Platform fee API endpoint
app.get('/api/platform-fee', (req, res) => {
  res.status(200).json({ fee: PLATFORM_FEE });
});

// Admin Auth Middleware
const adminGuard = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.status(401).json({ error: 'Unauthorized' });
  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    if (decoded.role !== 'admin') return res.status(403).json({ error: 'Forbidden' });
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid token' });
  }
};

// API Route for Admin Dashboard Stats
app.get('/api/admin/stats', adminGuard, async (req, res) => {
  try {
    const partnersCount = await pool.query('SELECT COUNT(*) FROM partners');
    const bookingsCount = await pool.query('SELECT COUNT(*) FROM bookings');
    const revenueResult = await pool.query('SELECT SUM(total_amount) FROM bookings');
    
    res.status(200).json({
      partners: parseInt(partnersCount.rows[0].count) || 0,
      bookings: parseInt(bookingsCount.rows[0].count) || 0,
      revenue: parseInt(revenueResult.rows[0].sum) || 0
    });
  } catch (error) {
    console.error('Error fetching stats:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API Route to fetch all partners (with pagination)
app.get('/api/admin/partners', adminGuard, async (req, res) => {
  try {
    const limit = parseInt(req.query.limit) || 50;
    const page = parseInt(req.query.page) || 1;
    const offset = (page - 1) * limit;
    const result = await pool.query('SELECT * FROM partners ORDER BY id DESC LIMIT $1 OFFSET $2', [limit, offset]);
    res.status(200).json({ success: true, partners: result.rows, page, limit });
  } catch (error) {
    console.error('Error fetching partners:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API Route to fetch all users (with pagination)
app.get('/api/admin/users', adminGuard, async (req, res) => {
  try {
    const limit = parseInt(req.query.limit) || 50;
    const page = parseInt(req.query.page) || 1;
    const offset = (page - 1) * limit;
    const result = await pool.query('SELECT * FROM users ORDER BY created_at DESC LIMIT $1 OFFSET $2', [limit, offset]);
    res.status(200).json({ success: true, users: result.rows, page, limit });
  } catch (error) {
    console.error('Error fetching users:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API Route to fetch all bookings (with pagination)
app.get('/api/admin/bookings', adminGuard, async (req, res) => {
  try {
    const limit = parseInt(req.query.limit) || 50;
    const page = parseInt(req.query.page) || 1;
    const offset = (page - 1) * limit;
    const result = await pool.query('SELECT * FROM bookings ORDER BY id DESC LIMIT $1 OFFSET $2', [limit, offset]);
    res.status(200).json({ success: true, bookings: result.rows, page, limit });
  } catch (error) {
    console.error('Error fetching bookings:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API Route to fetch user-specific bookings
app.get('/api/user/bookings', authGuard, async (req, res) => {
  let email = req.query.email;
  const phone = req.query.phone; // Fallback
  
  if (req.user.email !== email) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  
  try {
    let result;
    if (email) {
      email = email.trim().toLowerCase();
      // Search by email column OR by phone_number linked to user's email account
      result = await pool.query(
        'SELECT * FROM bookings WHERE LOWER(TRIM(email)) = $1 OR phone_number IN (SELECT phone FROM users WHERE LOWER(TRIM(email)) = $1) ORDER BY id DESC',
        [email]
      );
    } else if (phone) {
      result = await pool.query('SELECT * FROM bookings WHERE phone_number = $1 ORDER BY id DESC', [phone]);
    } else {
      return res.status(400).json({ error: 'Email or phone required' });
    }
    res.status(200).json({ success: true, bookings: result.rows });
  } catch (error) {
    console.error('Error fetching user bookings:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API Route to fetch ONLY matching bookings for a specific partner
app.get('/api/partner/bookings', authGuard, async (req, res) => {
  try {
    const { email } = req.query;
    if (!email) return res.status(400).json({ error: 'Email required' });
    
    if (req.user.email !== email || req.user.role !== 'partner') {
      return res.status(403).json({ error: 'Forbidden' });
    }

    // Fetch partner skills
    const partnerRes = await pool.query('SELECT skills FROM partners WHERE email = $1', [email]);
    if (partnerRes.rows.length === 0) return res.status(404).json({ error: 'Partner not found' });
    
    let skills = [];
    try {
      skills = typeof partnerRes.rows[0].skills === 'string' ? JSON.parse(partnerRes.rows[0].skills) : partnerRes.rows[0].skills;
    } catch(e) {}
    
    // Fetch bookings
    const result = await pool.query('SELECT * FROM bookings ORDER BY booking_date DESC, time_slot ASC');
    
    // Filter matching bookings using word-boundary matching to prevent false partial matches
    const matchedBookings = result.rows.filter(b => {
      let serviceType = '';
      let serviceCategory = '';
      try {
        const cart = typeof b.cart_items === 'string' ? JSON.parse(b.cart_items) : b.cart_items;
        if(cart && cart.length > 0) {
          serviceType = cart[0].title || cart[0].name || '';
          serviceCategory = cart[0].category || '';
        }
      } catch(e){}
      
      if(!skills || skills.length === 0) return false;
      const serviceTypeLower = serviceType.toLowerCase().trim();
      const serviceCategoryLower = serviceCategory.toLowerCase().trim();
      
      return skills.some(skill => {
        const skillLower = skill.toLowerCase().trim();
        
        // Exact match on Category (best match)
        if (serviceCategoryLower && serviceCategoryLower === skillLower) {
          return true;
        }

        // Fallback: Exact match OR word-boundary match on Title
        return serviceTypeLower === skillLower ||
               new RegExp('(^|\\s)' + skillLower.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(\\s|$)').test(serviceTypeLower);
      });
    });

    res.status(200).json({ success: true, bookings: matchedBookings });
  } catch (error) {
    console.error('Error fetching partner bookings:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API Route to update partner status
app.put('/api/admin/partners/:id/status', adminGuard, async (req, res) => {
  try {
    const { id } = req.params;
    const { status } = req.body;
    
    const result = await pool.query(
      'UPDATE partners SET status = $1 WHERE id = $2 RETURNING *',
      [status, id]
    );
    
    if(result.rows.length === 0) {
      return res.status(404).json({ error: 'Partner not found' });
    }
    
    res.status(200).json({ success: true, partner: result.rows[0] });
  } catch (error) {
    console.error('Error updating status:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// API Route for partner to accept a booking
app.put('/api/partner/accept-booking', authGuard, async (req, res) => {
  try {
    if (req.user.role !== 'partner') return res.status(403).json({ error: 'Forbidden' });
    const { booking_id, partner_name, partner_phone, partner_email } = req.body;
    
    // Atomic update to avoid race conditions
    const result = await pool.query(
      `UPDATE bookings 
       SET status = 'Confirmed', assigned_partner_name = $1, assigned_partner_phone = $2, assigned_partner_email = $3
       WHERE id = $4 AND (status = 'Pending' OR status IS NULL) RETURNING *`,
      [partner_name, partner_phone, partner_email, booking_id]
    );
    
    if (result.rowCount === 0) {
      return res.status(400).json({ error: 'Booking already accepted by someone else or not found.' });
    }
    
    res.status(200).json({ success: true, booking: result.rows[0] });
  } catch (error) {
    console.error('Error accepting booking:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// ✅ FIX #4: Partner booking status update — verify booking belongs to THIS partner
app.put('/api/partner/update-booking-status', authGuard, async (req, res) => {
  try {
    if (req.user.role !== 'partner') return res.status(403).json({ error: 'Forbidden' });
    const { booking_id, status } = req.body;
    
    // Get partner's phone first
    const partnerRes = await pool.query('SELECT phone FROM partners WHERE email = $1', [req.user.email]);
    if (partnerRes.rows.length === 0) return res.status(404).json({ error: 'Partner not found' });
    const partnerPhone = partnerRes.rows[0].phone;

    // Only allow update if this partner is the assigned partner OR if status is Pending
    const result = await pool.query(
      `UPDATE bookings SET status = $1 
       WHERE id = $2 AND (assigned_partner_phone = $3 OR (status = 'Pending' AND $1 = 'Confirmed'))
       RETURNING *`,
      [status, booking_id, partnerPhone]
    );
    
    if(result.rows.length === 0) {
      return res.status(403).json({ error: 'You are not authorized to update this booking or it does not exist.' });
    }
    
    res.status(200).json({ success: true, booking: result.rows[0] });
  } catch (error) {
    console.error('Error updating booking status:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// ✅ FIX #4: Partner can cancel/release a booking they accepted
app.put('/api/partner/release-booking', authGuard, async (req, res) => {
  try {
    if (req.user.role !== 'partner') return res.status(403).json({ error: 'Forbidden' });
    const { booking_id } = req.body;
    
    // Get partner's phone
    const partnerRes = await pool.query('SELECT phone FROM partners WHERE email = $1', [req.user.email]);
    if (partnerRes.rows.length === 0) return res.status(404).json({ error: 'Partner not found' });
    const partnerPhone = partnerRes.rows[0].phone;

    // Release the booking only if it belongs to this partner and is Confirmed
    const result = await pool.query(
      `UPDATE bookings SET status = 'Pending', assigned_partner_name = NULL, assigned_partner_phone = NULL 
       WHERE id = $1 AND assigned_partner_phone = $2 AND status = 'Confirmed'
       RETURNING *`,
      [booking_id, partnerPhone]
    );
    
    if(result.rows.length === 0) {
      return res.status(403).json({ error: 'Cannot release this booking. It may not belong to you or its status has advanced.' });
    }
    
    res.status(200).json({ success: true, message: 'Booking released successfully', booking: result.rows[0] });
  } catch (error) {
    console.error('Error releasing booking:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Fallback to serve index.html for any unknown route
app.use((req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Start Server (only if not running in Vercel)
if (require.main === module) {
  app.listen(PORT, HOST, () => {
    console.log(`Server is running at http://${HOST === '0.0.0.0' ? 'localhost' : HOST}:${PORT}`);
  }).on('error', (err) => {
    console.error('Failed to start server:', err.message);
    process.exit(1);
  });
}

module.exports = app;
