// URL de l'API
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Sélectionner l'élément avec l'ID 'character'
const characterElement = document.getElementById('character');

// Utiliser l'API Fetch pour récupérer les données
fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Erreur réseau : ' + response.status);
        }
        return response.json(); // Convertir la réponse en JSON
    })
    .then(data => {
        // Mettre à jour le texte de l'élément 'character' avec le nom du personnage
        characterElement.textContent = data.name;
    })
    .catch(error => {
        console.error('Il y a eu un problème avec la requête Fetch :', error);
        characterElement.textContent = 'Erreur de chargement du personnage';
    });
