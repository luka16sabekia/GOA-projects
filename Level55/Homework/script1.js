const form = document.getElementById('userForm');

form.addEventListener('submit', (event) => {
    event.preventDefault();
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    console.log(`Name: ${username}`);
    console.log(`Email: ${email}`);
    console.log(`Password: ${password}`);
});
