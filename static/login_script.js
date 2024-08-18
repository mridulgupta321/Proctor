const submitButton = document.getElementById("submit");
const signupButton = document.getElementById("sign-up");

const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");

const signupEmailIn = document.getElementById("email-signup");
const usernameIn = document.getElementById("username-signup");
const signupPasswordIn = document.getElementById("password-signup");
const confirmSignUpPasswordIn = document.getElementById("confirm-password-signup");
const dobIn = document.getElementById("dob-signup");
const genderIn = document.getElementById("gender-signup");
const mobileIn = document.getElementById("mobile-signup");
const createacctbtn = document.getElementById("create-acct-btn");

var email,
    password,
    signupEmail,
    username,
    signupPassword,
    confirmSignUpPassword,
    dob,
    gender,
    mobile;

createacctbtn.addEventListener("click", function(){
    var isVerified = true;

    signupEmail = signupEmailIn.value;
    signupPassword = signupPasswordIn.value;
    confirmSignUpPassword = confirmSignUpPasswordIn.value;
    username = usernameIn.value;
    dob = dobIn.value;
    gender = genderIn.value;
    mobile = mobileIn.value;

    if (signupPassword != confirmSignUpPassword){
        window.alert("Password fields do not match. Try again.");
        isVerified = false;
    }

    if (!signupEmail || !signupPassword || !confirmSignUpPassword || !dob || !gender || !mobile){
        window.alert("Please fill out all required fields.");
        isVerified = false;
    }

    const usernameIn = document.getElementById("username-signup");

    // Include username in the data sent to the server
    const data = {
        email: signupEmail,
        name: username,  // Added name field
        password: signupPassword,
        dob: dob,
        gender: gender,
        mobile: mobile
    };
    if (isVerified){
        var url = 'http://127.0.0.1:5000/signup_data';
        fetch(url, {
            method: 'POST',
            headers:{
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            if (data.status === 'success') {
                window.alert('Account created successfully!');
            } else {
                window.alert('Failed to create account: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            window.alert('An error occurred during account creation.');
        });
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
    };

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
                window.location.replace("./quiz_html");
            } else {
                window.alert("Login credentials don't match our database.");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            window.alert('An error occurred during login.');
        });
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
        } else {
            window.alert('Failed to create PDF');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        window.alert('An error occurred while creating PDF.');
    });
}
