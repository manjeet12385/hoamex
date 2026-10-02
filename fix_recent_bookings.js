const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

async function fixBookings() {
  await pool.query(`
    UPDATE bookings 
    SET cart_items = '[{"_v":2,"id":1790951918943,"price":999,"title":"Quick comfort therapy","imgSrc":"images/new_plumber_icon.jpg","quantity":1,"category":"Spa for Women"}]'
    WHERE id IN (11, 12);
  `);
  console.log("Updated bookings 11 and 12");
  process.exit(0);
}

fixBookings();
