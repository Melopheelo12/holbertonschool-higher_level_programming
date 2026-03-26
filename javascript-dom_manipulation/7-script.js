document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
    const list = document.getElementById('list_movies');
  
    fetch(url)
      .then(response => response.json())
      .then(data => {
        data.results.forEach(movie => {
          const li = document.createElement('li');
          li.textContent = movie.title;
          list.appendChild(li);
        });
      })
      .catch(error => {
        console.error('Error fetching movies:', error);
      });
  });