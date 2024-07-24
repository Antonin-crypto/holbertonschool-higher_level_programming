// Sélectionner l'élément avec l'ID 'red_header'
const redHeader = document.getElementById('red_header');

// Ajouter un écouteur d'événements pour le clic
redHeader.addEventListener('click', function() {
    // Sélectionner l'élément 'header'
    let header = document.querySelector('header');

    // Modifier la couleur du texte de l'élément 'header' en rouge
    header.style.color = '#FF0000';
});
