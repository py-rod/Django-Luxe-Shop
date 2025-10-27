const dropdown = document.querySelector(".dropdown-categories");
const btn = dropdown.querySelector("button");

btn.addEventListener("click", (e) => {
    e.stopPropagation();
    dropdown.classList.toggle("visible");
});

document.addEventListener("click", (e) => {
    if (!dropdown.contains(e.target)) {
        dropdown.classList.remove("visible");
    }
});
