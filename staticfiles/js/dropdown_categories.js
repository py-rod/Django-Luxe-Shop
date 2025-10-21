function myFunction() {
    let dropdownContent = document.getElementById("dropCategories");
    let dropdownCategories = document.querySelector(".dropdown-categories");

    if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
        dropdownCategories.classList.remove("visible");
    } else {
        dropdownContent.style.display = "block";
        dropdownCategories.classList.add("visible");
    }
}
