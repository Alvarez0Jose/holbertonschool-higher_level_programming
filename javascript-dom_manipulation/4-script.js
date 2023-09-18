const addItemButton = document.getElementById('add_item');
const myList = document.querySelector('.my_list');
addItemButton.addEventListener('click', function () {
    const NewItem = document.createElement('li');
    NewItem.textContent = 'Item';
    myList.appendChild(NewItem);
});
