import knex from 'knex';
import dotenv from 'dotenv';
dotenv.config();

const db = knex({
  client: 'pg',
  connection: {
    host: 'localhost',
    port: 5432,
    user: 'myuser',
    password: 'mypassword',
    database: 'mydb',
  },
});

export default db;
