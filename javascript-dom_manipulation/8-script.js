// Gets the div element 'hello'
const helloElement = document.getElementById('hello');

// Gets the translation from URL
fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Gets the translation from the response
        const translation = data.hello;

        // Display the translation in the hello element
        helloElement.textContent = translation;
    })
    .catch(error => {
        console.error('Error:', error);
    });
