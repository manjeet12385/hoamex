const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

async function checkBooking() {
  const result = await pool.query('SELECT id, cart_items FROM bookings WHERE id = 7');
  console.log(JSON.stringify(result.rows, null, 2));
  process.exit(0);
}

checkBooking();
