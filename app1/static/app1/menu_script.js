function openNav() {
    var element = document.getElementById("side_menu");

    if (element.style.width == "0px") {
        element.style.width = "250px";
    }
    else {
        element.style.width = "0px";
    }
}

function closeNav() {
    var element = document.getElementById("side_menu").style.width = "0px";
}