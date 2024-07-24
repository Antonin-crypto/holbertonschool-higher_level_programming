// Ajouter un écouteur d'événement pour s'assurer que le script s'exécute après le chargement complet du DOM
document.addEventListener('DOMContentLoaded', function() {
  // URL de l'API pour récupérer la traduction de "hello"
  const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Sélectionner l'élément avec l'ID 'hello'
  const helloElement = document.getElementById('hello');

  // Utiliser l'API Fetch pour récupérer les données
  fetch(url)
      .then(response => {
          if (!response.ok) {
              throw new Error('Erreur réseau : ' + response.status);
          }
          return response.json(); // Convertir la réponse en JSON
      })
      .then(data => {
          // Mettre à jour le texte de l'élément 'hello' avec la traduction de "hello"
          helloElement.textContent = data.hello;
      })
      .catch(error => {
          console.error('Il y a eu un problème avec la requête Fetch :', error);
          helloElement.textContent = 'Erreur de chargement';
      });
});
