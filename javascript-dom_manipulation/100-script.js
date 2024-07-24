document.addEventListener('DOMContentLoaded', function () {
    // Select the divs by their ids for add, remove, and clear actions
    const addItemButton = document.getElementById('add_item');
    const removeItemButton = document.getElementById('remove_item');
    const clearListButton = document.getElementById('clear_list');

    // Select the ul element with class 'my_list'
    const list = document.querySelector('.my_list');

    // Function to add a new item
    addItemButton.addEventListener('click', function() {
        const newItem = document.createElement('li');
        newItem.textContent = 'Item';
        list.appendChild(newItem);
    });

    // Function to remove the last item
    removeItemButton.addEventListener('click', function() {
        if (list.lastChild) {
            list.removeChild(list.lastChild);
        }
    });

    // Function to clear all items
    clearListButton.addEventListener('click', function() {
        while (list.firstChild) {
            list.removeChild(list.firstChild);
        }
    });
  });
