document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault();
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const gender = document.querySelector('input[name="gender"]:checked').value;
    const termsChecked = document.getElementById("terms").checked;
    if (!termsChecked) {
        alert("You must agree to the terms and conditions!");
        return;
    }
    console.log("Name:", name);
    console.log("Email:", email);
    console.log("Password:", password);
    console.log("Gender:", gender);
    alert("Registration successful!");
    document.getElementById("registrationForm").reset();
});
