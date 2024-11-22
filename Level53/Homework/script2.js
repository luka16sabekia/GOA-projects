const img = document.getElementById('myImage');
const button = document.getElementById('resizeButton');

button.addEventListener('click', function () {
    img.style.width = '300px';
    img.style.height = '300px';
});
