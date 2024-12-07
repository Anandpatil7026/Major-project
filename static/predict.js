// Get references to the input fields
var inputName = document.getElementById('name');
var inputAge = document.getElementById('age');
var inputBMI = document.getElementById('bmi');
var inputGlucose = document.getElementById('avgGlucoseLevel');
//var inputHBA1C = document.getElementById('hba1c');
//var inputCholesterol = document.getElementById('cholesterol');

// Get reference to the form
var form = document.querySelector('form');

// Function to validate name input
function validateName() {
    let name = inputName.value;
    if (name.length === 0 || !name.match(/^[A-Za-z]+(?: [A-Za-z]+)*$/)) {
        inputName.nextElementSibling.innerHTML = '<span class="wrong">❌ Please enter a valid name</span>';
        return false;
    }
    inputName.nextElementSibling.innerHTML = '<i class="check fa fa-check"></i>';
    return true;
}

// Function to validate age input
function validateAge() {
    let age = inputAge.value;
    if (age.length === 0) {
        inputAge.nextElementSibling.innerHTML = '<span class="wrong">❌ Please enter your age</span>';
        return false;
    }
    if (isNaN(age) || age < 10 || age > 90) {
        inputAge.nextElementSibling.innerHTML = '<span class="wrong">❌ Please enter a valid age (10-90)</span>';
        return false;
    }
    inputAge.nextElementSibling.innerHTML = '<i class="check fa fa-check"></i>';
    return true;
}

// Function to validate BMI input
function validateBMI() {
    let bmi = inputBMI.value;
    if (bmi.length === 0 || isNaN(bmi) || bmi < 15 || bmi > 45) {
        inputBMI.nextElementSibling.innerHTML = '<span class="wrong">❌ Please enter a valid BMI (15-45)</span>';
        return false;
    }
    inputBMI.nextElementSibling.innerHTML = '<i class="check fa fa-check"></i>';
    return true;
}

// Function to validate glucose level input
function validateGlucose() {
    let glucose = inputGlucose.value;
    if (glucose.length === 0 || isNaN(glucose) || glucose < 80 || glucose > 300) {
        inputGlucose.nextElementSibling.innerHTML = '<span class="wrong">❌ Please enter a valid glucose level (80-300)</span>';
        return false;
    }
    inputGlucose.nextElementSibling.innerHTML = '<i class="check fa fa-check"></i>';
    return true;
}



// Validate form on submission
form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    // Reset validation messages
    inputName.nextElementSibling.innerHTML = '';
    inputAge.nextElementSibling.innerHTML = '';
    inputBMI.nextElementSibling.innerHTML = '';
    inputGlucose.nextElementSibling.innerHTML = '';

    // Validate form fields
    if (!validateName() || !validateAge() || !validateBMI() || !validateGlucose()) {
        alert("Please fill out the form correctly!!");
        return false;
    }

    // If all validations pass, submit the form
    form.submit();
});

// Add event listeners for input fields
inputName.addEventListener('blur', validateName);
inputAge.addEventListener('blur', validateAge);
inputBMI.addEventListener('blur', validateBMI);
inputGlucose.addEventListener('blur', validateGlucose);