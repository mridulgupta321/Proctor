const submitButton = document.getElementById("submit");
const signupButton = document.getElementById("sign-up");

const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");

const main = document.getElementById("main");
const createacc = document.getElementById("create-acct");
const signupEmailIn = document.getElementById("email-signup");
const usernameIn = document.getElementById("username-signup");
const signupPasswordIn = document.getElementById("password-signup");
const confirmSignUpPasswordIn = document.getElementById("confirm-password-signup");
const createacctbtn = document.getElementById("create-acct-btn");
const forgetBtn = document.querySelector(".forget-btn")

var email,
    password,
    signupEmail,
    username,
    signupPassword,
    confirmSignUpPassword;

createacctbtn.addEventListener("click", function(){
    var isVerified = true;

    signupEmail = signupEmailIn.value;
    signupPassword = signupPasswordIn.value;
    confirmSignUpPassword = confirmSignUpPasswordIn.value;

    if (signupPassword != confirmSignUpPassword){
        window.alert("Password fields do not match. Try again.");
        isVerified = false;
    }

    username = usernameIn.value;
    if (!signupEmail || !signupPassword || !confirmSignUpPassword){
        window.alert("Please fill put all required fields.");
        isVerified = false;
    }

    const data = {
        signupEmail: signupEmail,
        username: username,
        signupPassword: signupPassword
    }
    // console.log(data)
    if (isVerified){
        var url = 'http://127.0.0.1:5000/signup_data';
        fetch(url, {
            method: 'POST', // or 'PUT'
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data) // data can be `string` or {object}!
        })
        .then(res => res.json())
        .then(data => console.log('Success:', window.alert(JSON.stringify(data))))
        .catch(error => console.error('Error:', error));
    }
});

submitButton.addEventListener("click", function() {
    var isVerified = true;
    email = emailInput.value;
    password = passwordInput.value;

    if (!email || !password) {
        window.alert("Please fill out all required fields.");
        isVerified = false;
    }

    const data = {
        email: email,
        password: password
    }

    if (isVerified) {
        var url = 'http://127.0.0.1:5000/login_data';
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            if (data.message !== 'Data not found!') {
                console.log('Login successful.');
                // Call the endpoint to run image_in_pdf
                runImageInPDF();
            } else {
                window.alert("Login credentials don't match our database.");
            }
        })
        .catch(error => console.error('Error:', error));
    }
});

function runImageInPDF() {
    fetch('http://127.0.0.1:5000/image_in_pdf', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            window.alert('PDF created successfully');
            window.location.replace("./quiz_html"); // Redirect after success
        } else {
            window.alert('Failed to create PDF');
        }
    })
    .catch(error => console.error('Error:', error));
}


// resetting a password
// forgetBtn.addEventListener("click", function(){
//     continue
// });