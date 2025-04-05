document.addEventListener("DOMContentLoaded", function () {
    const darkModeToggle = document.getElementById("darkModeToggle");
    const body = document.body;
    const navbar = document.getElementById("navbar");
    const navli = document.getElementById("navli");

    // Check for previously saved dark mode preference
    if (localStorage.getItem("darkMode") === "enabled") {
        enableDarkMode();
    }

    darkModeToggle.addEventListener("click", function () {
        if (body.classList.contains("bg-light")) {
            enableDarkMode();
        } else {
            disableDarkMode();
        }
    });

    function enableDarkMode() {
        body.classList.remove("bg-light");
        body.classList.add("bg-secondary", "text-white"); // Body Light Gray
        navbar.classList.remove("bg-secondary");
        navbar.classList.add("bg-dark", "navbar-dark"); // Navbar Dark Mode
        localStorage.setItem("darkMode", "enabled");
    }

    function disableDarkMode() {
        body.classList.remove("bg-secondary", "text-white");
        body.classList.add("bg-light","text-dark"); // Body Light Gray
        navbar.classList.remove("bg-dark", "navbar-dark");
        navbar.classList.add("bg-secondary"); // Navbar Light Mode
        localStorage.setItem("darkMode", "disabled");
    }
});
