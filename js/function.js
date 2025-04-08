const signUp = () => {
    document.getElementById("select").classList.add("hidden");
    document.getElementById("wlcm").classList.add("hidden");
    document.getElementById("signup").classList.remove("hidden");
    document.getElementById("backBtn").classList.remove("hidden");
}
const logIn = () => {
    document.getElementById("select").classList.add("hidden");
    document.getElementById("wlcm").classList.add("hidden");
    document.getElementById("login").classList.remove("hidden");
    document.getElementById("signup").classList.add("hidden");
    document.getElementById("backBtn").classList.remove("hidden");
}
const back = () => {
    document.getElementById("wlcm").classList.remove("hidden");
    document.getElementById("login").classList.add("hidden");
    document.getElementById("signup").classList.add("hidden");
    document.getElementById("backBtn").classList.add("hidden");
    document.getElementById("select").classList.remove("hidden");
}
const selection = () => {
    document.getElementById("log_in").classList.add("hidden");
    document.getElementById("wlcm").classList.add("hidden");
    document.getElementById("select").classList.remove("hidden");
}

const patient = () => {
    document.getElementById("wlcm").classList.remove("hidden");
    document.getElementById("signup").classList.add("hidden");
    document.getElementById("logHide").classList.remove("hidden");
    document.getElementById("backBtn").classList.add("hidden");
    document.getElementById("signLogin").classList.add("hidden");
    document.getElementById("select").classList.remove("hidden");

}
