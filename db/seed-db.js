import db from './db.js';

const genres = [
  { name: 'Action' },
  { name: 'Comedy' },
  { name: 'Drama' },
  { name: 'Sci-Fi' },
  { name: 'Horror' },
  { name: 'Romance' },
  { name: 'Thriller' },
  { name: 'Animation' },
  { name: 'Fantasy' },
  { name: 'Documentary' },
];

const movies = [
  { title: 'Inception', year: 2010, description: 'A thief who steals corporate secrets through dream-sharing technology.' },
  { title: 'The Godfather', year: 1972, description: 'The aging patriarch of an organized crime dynasty transfers control to his reluctant son.' },
  { title: 'Toy Story', year: 1995, description: 'A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy.' },
  { title: 'Parasite', year: 2019, description: 'Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.' },
  { title: 'The Dark Knight', year: 2008, description: 'Batman faces the Joker, a criminal mastermind who wants to plunge Gotham City into anarchy.' },
  { title: 'Forrest Gump', year: 1994, description: 'The presidencies of Kennedy and Johnson, the Vietnam War, and more through the eyes of Forrest Gump.' },
  { title: 'Interstellar', year: 2014, description: 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity’s survival.' },
  { title: 'Spirited Away', year: 2001, description: 'During her family’s move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, spirits, and witches.' },
  { title: 'Pulp Fiction', year: 1994, description: 'The lives of two mob hitmen, a boxer, a gangster’s wife, and a pair of diner bandits intertwine.' },
  { title: 'The Matrix', year: 1999, description: 'A computer hacker learns about the true nature of his reality and his role in the war against its controllers.' },
  { title: 'Titanic', year: 1997, description: 'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.' },
  { title: 'Get Out', year: 2017, description: 'A young African-American visits his white girlfriend’s parents for the weekend.' },
  { title: 'Finding Nemo', year: 2003, description: 'After his son is captured in the Great Barrier Reef and taken to Sydney, a timid clownfish sets out on a journey to bring him home.' },
  { title: 'Avengers: Endgame', year: 2019, description: 'After the devastating events of Infinity War, the universe is in ruins.' },
  { title: 'Joker', year: 2019, description: 'In Gotham City, mentally troubled comedian Arthur Fleck is disregarded and mistreated by society.' },
  { title: 'Coco', year: 2017, description: 'Aspiring musician Miguel, confronted with his family’s ancestral ban on music, enters the Land of the Dead.' },
  { title: 'The Shawshank Redemption', year: 1994, description: 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.' },
  { title: 'The Lion King', year: 1994, description: 'Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.' },
  { title: 'Alien', year: 1979, description: 'After a space merchant vessel receives an unknown transmission as a distress call, one of the crew is attacked by a mysterious lifeform.' },
  { title: 'Blade Runner', year: 1982, description: 'A blade runner must pursue and terminate four replicants who stole a ship in space and have returned to Earth to find their creator.' },
];

const movieGenres = [
  { movie: 'Inception', genres: ['Action', 'Sci-Fi', 'Thriller'] },
  { movie: 'The Godfather', genres: ['Drama', 'Crime'] },
  { movie: 'Toy Story', genres: ['Animation', 'Comedy', 'Fantasy'] },
  { movie: 'Parasite', genres: ['Drama', 'Thriller'] },
  { movie: 'The Dark Knight', genres: ['Action', 'Drama', 'Thriller'] },
  { movie: 'Forrest Gump', genres: ['Drama', 'Romance'] },
  { movie: 'Interstellar', genres: ['Sci-Fi', 'Drama', 'Adventure'] },
  { movie: 'Spirited Away', genres: ['Animation', 'Fantasy'] },
  { movie: 'Pulp Fiction', genres: ['Crime', 'Drama'] },
  { movie: 'The Matrix', genres: ['Action', 'Sci-Fi'] },
  { movie: 'Titanic', genres: ['Drama', 'Romance'] },
  { movie: 'Get Out', genres: ['Horror', 'Thriller'] },
  { movie: 'Finding Nemo', genres: ['Animation', 'Adventure'] },
  { movie: 'Avengers: Endgame', genres: ['Action', 'Sci-Fi', 'Adventure'] },
  { movie: 'Joker', genres: ['Crime', 'Drama', 'Thriller'] },
  { movie: 'Coco', genres: ['Animation', 'Fantasy', 'Adventure'] },
  { movie: 'The Shawshank Redemption', genres: ['Drama', 'Crime'] },
  { movie: 'The Lion King', genres: ['Animation', 'Drama', 'Adventure'] },
  { movie: 'Alien', genres: ['Sci-Fi', 'Horror'] },
  { movie: 'Blade Runner', genres: ['Sci-Fi', 'Thriller'] },
];

async function seed() {
  await db('movie_genres').del();
  await db('movies').del();
  await db('genres').del();

  // Insert genres
  const genreIds = {};
  for (const genre of genres) {
    const ret = await db('genres').insert(genre).returning('id');
    // knex returning array of objects: [{id: 1}]
    const id = typeof ret[0] === 'object' ? ret[0].id : ret[0];
    genreIds[genre.name] = id;
  }

  // Insert movies
  const movieIds = {};
  for (const movie of movies) {
    const ret = await db('movies').insert(movie).returning('id');
    const id = typeof ret[0] === 'object' ? ret[0].id : ret[0];
    movieIds[movie.title] = id;
  }

  // Insert movie_genres
  for (const mg of movieGenres) {
    for (const genreName of mg.genres) {
      if (genreIds[genreName] && movieIds[mg.movie]) {
        await db('movie_genres').insert({
          movie_id: movieIds[mg.movie],
          genre_id: genreIds[genreName],
        });
      }
    }
  }

  console.log('Seeded database with movies and genres!');
  await db.destroy();
}

seed();
