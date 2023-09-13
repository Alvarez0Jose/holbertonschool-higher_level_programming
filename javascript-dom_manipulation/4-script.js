// Gets element with id "add_item"
const addItemButton = document.getElementById('add_item');

// Get the <UL? element with class "my_list"
const myList = document.querySelector('.my_list');

// Adds a Listener event
addItemButton.addEventListener('click', function () {
    // Creates a new <li> element
    const NewItem = document.createElement('li');

    // Sets the text content of the new element
    NewItem.textContent = 'Item';

    // Append the new element to myList
    myList.appendChild(NewItem);
});
