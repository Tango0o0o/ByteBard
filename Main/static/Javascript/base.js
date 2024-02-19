const url = window.location.href;
const primary_tabs = ["login", "register", "profile"]; // The biggest tabs at the top of the navbar (their id's)
let tab_selected = false;

primary_tabs.forEach(tab => {
    if (url.includes(tab)){ // check each tab name
        classname = document.getElementById(tab).className;
        document.getElementById(tab).className = classname + " selected"; 
        tab_selected = true;
        // keeping the original class name (for they positioning/styling), than also added selected class
    }
});

if (!tab_selected) { // if none other tabs are selected then it must be the home page.
    console.log(tab_selected);
    classname = document.getElementById("home").className;
    document.getElementById("home").className = classname + " selected"; 
};