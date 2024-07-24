// Sélectionner l'élément avec l'ID 'toggle_header'
var toggleHeader = document.getElementById('toggle_header');

// Ajouter un écouteur d'événements pour le clic
toggleHeader.addEventListener('click', function() {
    // Sélectionner l'élément 'header'
    var header = document.querySelector('header');

    // Basculer la classe du 'header' entre 'red' et 'green'
    if (header.classList.contains('red')) {
        header.classList.remove('red');
        header.classList.add('green');
    } else {
        header.classList.remove('green');
        header.classList.add('red');
    }
});
