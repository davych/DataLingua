import db from '../db.js';

export const searchMoviesByTitleFuzzy = async (title) => {
  const res = await db('movies').select('id', 'title', 'year').where('title', 'ILIKE', `%${title}%`);
  return res;
}

// searchMoviesBy genre name
export const searchMoviesByGenreName = async (genreName) => {
  const res = await db('movies')
    .join('movie_genres', 'movies.id', 'movie_genres.movie_id')
    .join('genres', 'movie_genres.genre_id', 'genres.id')
    .select('movies.id', 'movies.title', 'movies.year')
    .where('genres.name', 'ILIKE', `%${genreName}%`);
  return res;
}

// get all movies
export const getAllMovies = async () => {
  const res = await db('movies').select('id', 'title', 'year');
  return res;
}