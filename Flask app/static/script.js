document.getElementById('myForm').addEventListener('submit', function() {
    // Code to be executed when the button is clicked
    event.preventDefault();

    const num1 = document.getElementById('numberOne').value;
    const num2 = document.getElementById('numberTwo').value;
    // console.log(numberOne, numberTwo);

    fetch('/process_form', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ number1: num1, number2: num2 }),
    })
    .then(response=>response.json())
    .then(data=>alert('Sum of ' + num1 + ' and ' + num2 + ' is: ' + data.result))
    .catch(error => 
        console.error('Error:', error));
});