document.getElementById('executeButton').addEventListener('click', function() {
    // When the button is clicked, send a request to the backend
    fetch('/execute_function', {
        method: 'POST',
    })
    .then(response => response.text())
    .then(data => {
        console.log(data);
        // Handle the response from the backend if needed
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('numberForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get the entered number
    const enteredNumber = document.getElementById('numberInput').value;

    // Send the number to the backend (you can use fetch or another method)
    // Example using fetch:
    fetch('/backend-endpoint', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ number: enteredNumber }),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Response from backend:', data);
        // Handle the response if needed
    })
    .catch(error => console.error('Error:', error));
});