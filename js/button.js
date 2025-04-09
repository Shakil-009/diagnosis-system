const container = document.querySelector('.buttons-container');

for (let i = 0; i < 26; i++) {
    const button = document.createElement('button');
    button.textContent = String.fromCharCode(65 + i);
    container.appendChild(button);
}

document.getElementById("logOut").addEventListener("click",function (){
    window.location.href = "index.html"
})