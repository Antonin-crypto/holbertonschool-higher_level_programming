// Sélectionner l'élément avec l'ID 'red_header'
var redHeader = document.getElementById('red_header');

// Ajouter un écouteur d'événements pour le clic
redHeader.addEventListener('click', function() {
    // Sélectionner l'élément 'header'
    var header = document.querySelector('header');

    // Ajouter la classe 'red' à l'élément 'header'
    header.classList.add('red');
});
