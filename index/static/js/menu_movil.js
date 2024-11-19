// Función para abrir/cerrar el menú desplegable
function toggleDropdownMovil() {
    let dropdown = document.getElementById("myDropdown");
    dropdown.classList.toggle("open");
}

document.addEventListener("click", function (event) {
    let dropdown = document.getElementById("myDropdown");
    if (!event.target.closest('.dropdownProfile') && dropdown.classList.contains('open')) {
        dropdown.classList.remove('open');
    }
});
