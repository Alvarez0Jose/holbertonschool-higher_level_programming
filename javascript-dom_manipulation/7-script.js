// Gets the ul element in "list_movies"
const listMoviesElement = document.getElementById('list_movies');

// Gets the movie data from URL
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Extracts the data from response
        const movies = data.results;

        // Loops through movies and adds titles
        movies.forEach(movie => {
            const movieTitle = movie.title;
            const listItem = document.createElement('li');
            lisstItem.textContent = movieTitle;
            listMoviesElement.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
