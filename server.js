require('dotenv').config();
const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const { Pool } = require('pg');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Connect to Neon PostgreSQL
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false
  }
});

// Middleware
app.use(cors());
app.use(bodyParser.json());
// Serve the static HTML/JS/CSS files from this directory
app.use(express.static(path.join(__dirname, '')));

// Initialize Database Table
async function initDb() {
  try {
    await pool.query(`
      CREATE TABLE IF NOT EXISTS bookings (
        id SERIAL PRIMARY KEY,
        customer_name VARCHAR(100),
        phone_number VARCHAR(20),
        address TEXT,
        landmark TEXT,
        booking_date DATE,
        time_slot VARCHAR(50),
        payment_method VARCHAR(50),
        cart_items JSONB,
        total_amount INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `);
    console.log("Database table 'bookings' is ready!");
  } catch (error) {
    console.error("Error initializing database:", error);
  }
}
initDb();

// API Route to handle new bookings
app.post('/api/bookings', async (req, res) => {
  try {
    const { 
      customer_name, 
      phone_number, 
      address, 
      landmark, 
      booking_date, 
      time_slot, 
      payment_method, 
      cart_items, 
      total_amount 
    } = req.body;

    // Validate simple required fields
    if (!customer_name || !phone_number || !cart_items || cart_items.length === 0) {
      return res.status(400).json({ error: 'Missing required fields or empty cart' });
    }

    const query = `
      INSERT INTO bookings 
      (customer_name, phone_number, address, landmark, booking_date, time_slot, payment_method, cart_items, total_amount) 
      VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
      RETURNING *;
    `;
    
    const values = [
      customer_name, 
      phone_number, 
      address, 
      landmark, 
      booking_date, 
      time_slot, 
      payment_method, 
      JSON.stringify(cart_items), 
      total_amount
    ];

    const result = await pool.query(query, values);
    
    res.status(201).json({ 
      message: 'Booking created successfully!', 
      booking: result.rows[0] 
    });

  } catch (error) {
    console.error('Error saving booking:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});

// Fallback to serve index.html for any unknown route
app.use((req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Start Server
app.listen(PORT, () => {
  console.log(`Server is running at http://localhost:${PORT}`);
});
