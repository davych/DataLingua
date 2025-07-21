import db from '../db.js';

export const searchGenresByFuzzyName = async (name) => {
  const res = await db('genres').select('id', 'name').where('name', 'ILIKE', `%${name}%`);
  return res;
}
// get all genres
export const getAllGenres = async () => {
  const res = await db('genres').select('id', 'name');
  return res;
}