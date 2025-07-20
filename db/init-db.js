import db from './db.js';

async function main() {
  await db.schema.dropTableIfExists('movies');
  await db.schema.dropTableIfExists('genres');
  await db.schema.dropTableIfExists('movie_genres');

  await db.schema.createTable('genres', (table) => {
    table.increments('id').primary();
    table.string('name').notNullable();
  });

  await db.schema.createTable('movies', (table) => {
    table.increments('id').primary();
    table.string('title').notNullable();
    table.integer('year');
    table.text('description');
  });

  await db.schema.createTable('movie_genres', (table) => {
    table.integer('movie_id').references('id').inTable('movies').onDelete('CASCADE');
    table.integer('genre_id').references('id').inTable('genres').onDelete('CASCADE');
    table.primary(['movie_id', 'genre_id']);
  });

  console.log('Tables created!');
  await db.destroy();
}

main();
