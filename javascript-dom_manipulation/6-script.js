const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then(response => {
    return response.json();
  })
  .then(data => {
    const characterName = data.name;

    const characterDiv = document.querySelector('#character');

    characterDiv.textContent = characterName;
  })
  .catch(error => {
    console.error('Erreur lors de la récupération :', error);
  });
