const field_ids = ["id_email", "id_password1", "id_username", "id_first_name", "id_last_name"] // id of the form fields

for (const id of field_ids) { // This will loop through every element in the form field
    // And then procced to change the class of the input depending on whether it is valid or not

    let input = document.getElementById(id); // Form field
    const value = input.value; // The input of the form field (valid or invalid)

    input.addEventListener('input', function() // Triggered when input is enter in text field
        {
            if (value != input.value) { // 1. Checking if the invalid input has been changed
                input.className = "form-input"; // See register.css // 1. If so then change it to the normal input field
                document.getElementById(id+"-error-message").style.display = "none" // Hide the error message
            }

            else {
                input.className = "form-input invalid"; // See register.css // 1. If not then put it on the invalid class
                document.getElementById(id+"-error-message").style.display = "block" // Make the error message visible
            }
        }
    );
}