require('dotenv').config();
const { Pool } = require('pg');
const pool = new Pool({ connectionString: process.env.DATABASE_URL });

async function run() {
  const res = await pool.query("SELECT email, skills FROM partners WHERE skills::text ILIKE '%Solar Water Heater%'");
  console.log('PARTNERS:', JSON.stringify(res.rows, null, 2));
  
  const bres = await pool.query("SELECT id, cart_items FROM bookings ORDER BY booking_date DESC LIMIT 5");
  console.log('BOOKINGS:', JSON.stringify(bres.rows, null, 2));
  process.exit(0);
}
run();
