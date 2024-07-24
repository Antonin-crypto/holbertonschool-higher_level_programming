// Sélectionner l'élément avec l'ID 'update_header'
var updateHeader = document.getElementById('update_header');

// Ajouter un écouteur d'événements pour le clic
updateHeader.addEventListener('click', function() {
    // Sélectionner l'élément 'header'
    var header = document.querySelector('header');

    // Mettre à jour le texte de l'élément 'header'
    header.textContent = 'New Header!!!';
});
