document.addEventListener("DOMContentLoaded", function () {
    const darkModeToggle = document.getElementById("darkModeToggle");
    const body = document.body;

    // Check Local Storage for Dark Mode Preference
    if (localStorage.getItem("dark-mode") === "enabled") {
        enableDarkMode();
    }

    darkModeToggle.addEventListener("click", function () {
        if (body.classList.contains("dark-mode")) {
            disableDarkMode();
        } else {
            enableDarkMode();
        }
    });

    function enableDarkMode() {
        body.classList.add("dark-mode");
        darkModeToggle.innerHTML = "☀️"; // Change icon to Sun
        localStorage.setItem("dark-mode", "enabled");
    }

    function disableDarkMode() {
        body.classList.remove("dark-mode");
        darkModeToggle.innerHTML = "🌙"; // Change icon to Moon
        localStorage.setItem("dark-mode", "disabled");
    }
});
