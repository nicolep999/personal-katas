function moviesInfo(input) {
  const movies = [];

  for (const line of input) {
    if (line.startsWith("addMovie ")) {
      const name = line.replace("addMovie ", "");
      movies.push({ name });
    } else if (line.includes(" directedBy ")) {
      const [name, director] = line.split(" directedBy ");
      const movie = movies.find((m) => m.name === name);
      if (movie) {
        movie.director = director;
      }
    } else if (line.includes(" onDate ")) {
      const [name, date] = line.split(" onDate ");
      const movie = movies.find((m) => m.name === name);
      if (movie) {
        movie.date = date;
      }
    }
  }

  for (const movie of movies) {
    if (movie.name && movie.director && movie.date) {
      console.log(JSON.stringify(movie));
    }
  }
}
