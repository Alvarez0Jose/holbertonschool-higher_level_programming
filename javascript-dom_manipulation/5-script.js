// Gets element with id "update_header"
const updateHeaderButton = document.getElementById('update_header');

// get the <header> element
const headerElement = document.querySelector('header');

// Add and event listener
updateHeaderButton.addEventListener('click', fucntion () {
    // Updates the text of the content
    headerElement.textContent = 'New Header!!!';

});
