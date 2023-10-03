
var i, checkboxes = document.querySelectorAll('input[type=checkbox]');

function save() {
    for (i=0; i < checkboxes.length; i++) {
        localStorage.setItem(checkboxes[i].ariaValueMax, checkboxes[i].checked);
    }
}

function load_() {
    for (let i = 0; i < checkboxes.length; i++) {
        checkboxes[i].checked = localStorage.getItem(checkboxes[i].value) === 'true' ? true:false;
        
    }
}