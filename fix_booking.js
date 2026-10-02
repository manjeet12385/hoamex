const { Pool } = require('pg');
require('dotenv').config();

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: false }
});

async function fixBooking() {
  const cartItems = [
    {
      "_v": 2,
      "id": 1790950739000,
      "price": 1888,
      "title": "Sublime Swedish with head massage",
      "imgSrc": "http://localhost:3000/images/womens_spa.jpg",
      "quantity": 1,
      "category": "Spa for Women"
    }
  ];
  await pool.query('UPDATE bookings SET cart_items = $1 WHERE id = 7', [JSON.stringify(cartItems)]);
  console.log("Updated booking 7");
  process.exit(0);
}

fixBooking();
