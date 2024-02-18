const url = window.location.href;
const primary_tabs = ["login", "register"]; // The biggest tabs at the top of the navbar
let tab_selected = false;

primary_tabs.forEach(tab => {
    if (url.includes(tab)){
        console.log(tab);
        classname = document.getElementById(tab).className;
        document.getElementById(tab).className = classname + " selected"; 
        console.log("ds");
        tab_selected = true;
        // keeping the original class name (for they positioning/styling), than also added selected class
    }
});

if (!tab_selected) {
    console.log(tab_selected);
    classname = document.getElementById("home").className;
    document.getElementById("home").className = classname + " selected"; 
    console.log("fd");
};