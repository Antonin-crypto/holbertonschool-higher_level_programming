// Sélectionner l'élément avec l'ID 'add_item'
const addItem = document.getElementById('add_item');

// Ajouter un écouteur d'événements pour le clic
addItem.addEventListener('click', function() {
    // Créer un nouvel élément 'li'
    let newLi = document.createElement('li');
    newLi.textContent = 'Item';

    // Sélectionner la liste 'ul' avec la classe 'my_list'
    let myList = document.querySelector('ul.my_list');

    // Ajouter le nouvel élément 'li' à la liste
    myList.appendChild(newLi);
});
