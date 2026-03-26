// On définit l'URL de l'API Star Wars (SWAPI)
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// On utilise fetch pour envoyer une requête réseau
fetch(url)
  .then(response => {
    // La réponse arrive d'abord sous forme de flux brut.
    // On la convertit en objet JSON (JavaScript Object).
    return response.json();
  })
  .then(data => {
    // Une fois le JSON extrait, on accède à la propriété "name"
    const characterName = data.name;

    // On sélectionne l'élément HTML avec l'ID "character"
    const characterDiv = document.querySelector('#character');

    // On met à jour le contenu de la div avec le nom reçu
    characterDiv.textContent = characterName;
  })
  .catch(error => {
    // Toujours une bonne pratique de gérer les erreurs (ex: coupure internet)
    console.error('Erreur lors de la récupération :', error);
  });