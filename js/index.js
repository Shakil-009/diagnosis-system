document.getElementById("login").classList.add("hidden");
document.getElementById("signup").classList.add("hidden");
const login = () => {
    const password = document.getElementById("password").value;
    const email = document.getElementById("email").value;
    const specialChars = "._-+@";
    if(typeof email !== 'string')
    {
        return '"Invalid"';
    }
    if(specialChars.includes(email[0]) || email.includes(" ") || !email.endsWith(".com") || typeof email !== 'string' || (email.match(/@/g) || []).length !== 1)
    {
        alert("Please put a valid email")
    }

    else {
        if(password == 1234)
            {
                alert('Successfully logged in');
            }
            else{
                alert("Wrong password");
            }
    }
}