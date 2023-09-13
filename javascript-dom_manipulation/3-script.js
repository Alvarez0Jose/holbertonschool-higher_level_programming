// Gets element with "toggle_header"
const toggleHeader = document.getElementById('toggle_header');

// Gets the header element
const headerElement = documemt.querySlector('header');

// Add an event listner for click on the toggle element
toggleHeader.addEventListener('click', fucntion () {
    // checks the current class of the header element
    if (headerElement.classList.contains('red')) {
        // cchanges 'red' for 'green'
        headerElement.classList.remove('red');
        headerElement.classList.add('green');
    } else {
        // If class has 'green' or no class, remove it and add 'red'
        headerElement.classList.remove('green');
        headerElement.classList.add('red');
    }
});
