function openUrl() {
    var username = document.getElementById("username-input").value;
    var password = document.getElementById("password-input").value;

    if (username !== "" && password !== "") {
        var urlWithParam = "/home/" + username;
        window.open(urlWithParam);
    } else {
        alert("Please enter a username and a password!")
    }
}

function notImplemented() {
    alert("This is not implemented yet. But you can use any username and password combination.")
}
