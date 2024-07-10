const form = document.getElementById('adminregister');
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // confirm register
    var isRegister = confirm("Are you sure you want to register your Barangay Profile?");

    if (!isRegister) return;


    let formFields = document.getElementsByClassName('form-field');

    let spaceRegex = /\s+/;
    let specialChars = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;
    
    for (let i = 0; i < formFields.length; i++) {

        if (formFields[i].name == 'password1' || formFields[i].name == 'password2') {
            //? regex check if value is empty or has consecutive spaces
            if (spaceRegex.test(formFields[i].value) || formFields[i].value === '' || formFields[i].value === null) {
                alert('Password should be non-empty and should not contain consecutive spaces');
                return;
            }
        }

        if (specialChars.test(formFields[i].value)) {
            alert('Please do not use special characters in ' + formFields[i].name);
            return;
        }

        //?  check if value is empty or has consecutive spaces
        if (!isNaN(formFields[i].value)) {
            alert('Please input a valid value for ' + formFields[i].name);
            return;
        }
        
    }

    form.submit();

});



