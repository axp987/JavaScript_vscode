
//const Loginform = document.querySelector("login-form");
//const LoginInput = Loginform.querySelector("input");
//const LoginButton = Loginform.querySelector("button");

const Loginform = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeTing = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden";
const USERNAME_KEY = "username";
const getUsername = localStorage.getItem(USERNAME_KEY);


function onLoginSubmit(event) {
    event.preventDefault();
    const username = loginInput.value;
    Loginform.classList.add(HIDDEN_CLASSNAME);
    localStorage.setItem(USERNAME_KEY, username);
    notNullApllication(username);
}

function notNullApllication(username) {
    greeTing.classList.remove(HIDDEN_CLASSNAME);
    greeTing.innerText=`Nice Meet you ${username}`;
}

if(getUsername === null) {
    Loginform.classList.remove(HIDDEN_CLASSNAME);
    Loginform.addEventListener("submit", onLoginSubmit);
}
else {
    notNullApllication(getUsername);
}