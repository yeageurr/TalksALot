const log = console.log;
const usernameInput = document.getElementById('username');
const passwordInput = document.getElementById('password');
const passwordDiv = document.getElementById('passwDiv');
const confirmPassDiv = document.getElementById('cpasswDiv');
const confirmPassInput = document.getElementById('confirmPass');
const emailInput = document.getElementById('email');
const termsBox = document.getElementById('terms');

function check_empty_values(val, field) {
  if (val.value.trim().length == 0) {
    alert(`${field} cannot be empty!`);
    return false;
  }
  return true;
}

function validate(e) {
  e.preventDefault();
  const password_pattern = /^(?=.*[A-Za-z])(?=.*\d).{8,}$/;

  // Check for empty fields
  if(!check_empty_values(usernameInput, 'username')) {
    usernameInput.classList.add("error");
    return
  } else {
    usernameInput.classList.remove("error");
  }

  // Validate inputs
  if( !password_pattern.test(passwordInput.value.trim()) ) {
    alert("Password must contain digits and letters and at least 8-character long.");
    passwordDiv.classList.add("error");
    return;
  } else {
    passwordDiv.classList.remove("error");
    if(confirmPassInput.value.trim() != passwordInput.value.trim()) {
      alert("Passwords does not match!");
      confirmPassDiv.classList.add("error");
      return;
    } else {
      confirmPassDiv.classList.remove("error");
    }
  }

  if(!check_empty_values(emailInput, 'email')) {
    emailInput.classList.add("error");
    return
  } else {
    if(emailInput.value.endsWith("@spam.com") ) {
      alert("Email is invalid!");
      emailInput.classList.add("error");
      return;
    }
    emailInput.classList.remove("error");
  }

  if(!termsBox.checked) {
    alert("Please agree to the Terms and Policies to continue");
    return;
  }

  alert("Registered!")
}