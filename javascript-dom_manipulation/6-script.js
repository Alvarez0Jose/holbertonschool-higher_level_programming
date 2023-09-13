// Gets element with id "character"
const characterElement = document.getElementById('character');

// Gets the character data from URL
fetch('https://swapi-api.hbtn.io/api/people/5?format=json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Extracts the character name
        const characterName = data.name;

        // Displays the characters name
        characterElement.textContent = characterName;
    })
    .catch(error => {
        console.error('Error:', error);
    });
