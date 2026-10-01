require('dotenv').config();
const { Pool } = require('pg');

const pool = new Pool({ 
  connectionString: process.env.DATABASE_URL, 
  ssl: { rejectUnauthorized: false } 
});

async function createTable() {
  const query = `
    CREATE TABLE IF NOT EXISTS partners (
      id SERIAL PRIMARY KEY,
      full_name VARCHAR(255) NOT NULL,
      email VARCHAR(255) UNIQUE NOT NULL,
      phone VARCHAR(20) NOT NULL,
      experience_years VARCHAR(50),
      primary_category VARCHAR(100),
      skills JSONB,
      documents JSONB,
      bank_details JSONB,
      status VARCHAR(50) DEFAULT 'PENDING',
      joined_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
  `;
  try {
    await pool.query(query);
    console.log('Partners table created successfully!');
  } catch (err) {
    console.error('Error creating table:', err);
  } finally {
    pool.end();
  }
}

createTable();
