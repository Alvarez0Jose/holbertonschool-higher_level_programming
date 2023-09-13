// Gets element with id "red_header"
const redHeader = document.getElementById('red_header');

// Adds a click listener
redHeader.addEventListener('click', function () {
    // Add the "red" class to the header element
    const headerElement = document.querySelector('header');
    headerElement.classList.add('red');
});
