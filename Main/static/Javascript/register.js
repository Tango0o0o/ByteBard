const field_ids = ["id_email", "id_password1", "id_username", "id_first_name", "id_last_name"] // id of the form fields

for (const id of field_ids) { // This will loop through every element in the form field
    // And then procced to change the class of the input depending on whether it is valid or not

    let field = document.getElementById(id);
    if (field.hasAttribute("error")) { 
        // If the field has the attribute error, this means hat there is an error in the field, and this code should apply to that field
       
        const value = field.value; // The value of the form field

        field.addEventListener('input', function() // Triggered when input is enter in text field
            {
                if (value != field.value) { // 1. Checking if the invalid input has been changed
                    field.className = "form-input"; // See register.css // 1. If so then change it to the normal input field
                    document.getElementById(id+"-error-message").style.display = "none" // Hide the error message
                }

                else {
                    field.className = "form-input invalid"; // See register.css // 1. If not then put it on the invalid class
                    document.getElementById(id+"-error-message").style.display = "block" // Make the error message visible
                }
            }
        );
    }
}


// TEST ON PROFILE PAGE, ERROR FIXED ON REGITSER THOUGH