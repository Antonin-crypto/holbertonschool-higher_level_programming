// Sélectionner l'élément avec l'ID 'add_item'
var addItem = document.getElementById('add_item');

// Ajouter un écouteur d'événements pour le clic
addItem.addEventListener('click', function() {
    // Créer un nouvel élément 'li'
    var newLi = document.createElement('li');
    newLi.textContent = 'Item';

    // Sélectionner la liste 'ul' avec la classe 'my_list'
    var myList = document.querySelector('ul.my_list');

    // Ajouter le nouvel élément 'li' à la liste
    myList.appendChild(newLi);
});
