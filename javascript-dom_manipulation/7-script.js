// URL de l'API pour les films
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Sélectionner l'élément avec l'ID 'list_movies'
const listMoviesElement = document.getElementById('list_movies');

// Utiliser l'API Fetch pour récupérer les données des films
fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Erreur réseau : ' + response.status);
        }
        return response.json(); // Convertir la réponse en JSON
    })
    .then(data => {
        // Parcourir les films et créer un élément <li> pour chaque titre
        data.results.forEach(film => {
            const listItem = document.createElement('li');
            listItem.textContent = film.title;
            listMoviesElement.appendChild(listItem);
        });
    })
    .catch(error => {
        console.error('Il y a eu un problème avec la requête Fetch :', error);
        listMoviesElement.textContent = 'Erreur de chargement des films';
    });
