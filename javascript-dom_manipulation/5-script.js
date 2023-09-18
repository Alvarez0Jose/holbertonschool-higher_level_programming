const updateHeaderButton = document.getElementById('update_header');
const headerElement = document.querySelector('header');
updateHeaderButton.addEventListener('click', fucntion () {
    headerElement.textContent = 'New Header!!!';

});
