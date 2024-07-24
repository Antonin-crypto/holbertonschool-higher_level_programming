// Sélectionner l'élément avec l'ID 'update_header'
const updateHeader = document.getElementById('update_header');

// Ajouter un écouteur d'événements pour le clic
updateHeader.addEventListener('click', function() {
    // Sélectionner l'élément 'header'
    const header = document.querySelector('header');

    // Mettre à jour le texte de l'élément 'header'
    header.textContent = 'New Header!!!';
});
