require('dotenv').config();
const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false
  }
});

async function checkDb() {
  try {
    const res = await pool.query('SELECT * FROM users');
    console.log("Users:", res.rows);
  } catch (err) {
    console.error("Query Error:", err.message);
  } finally {
    pool.end();
  }
}

checkDb();
