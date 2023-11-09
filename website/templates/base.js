document.addEventListener("DOMContentLoaded", function () {
    const discoButton = document.getElementById("discoButton");
    const starWarsButton = document.getElementById("starWarsButton");
    const htmlElement = document.documentElement;
    const header = document.querySelector("header");
    const buttons = document.querySelectorAll("button");
    const crawl = document.querySelector(".crawl");

    discoButton.addEventListener("click", function () {
        // Start the disco effect
        header.classList.add("disco-active");
        buttons.forEach(button => {
            button.classList.add("disco-active");
        });

        // Remove the disco effect after 3 seconds
        setTimeout(function () {
            header.classList.remove("disco-active");
            buttons.forEach(button => {
                button.classList.remove("disco-active");
            });
        }, 3000); // 3000 milliseconds (3 seconds)

        // Apply Star Wars theme
        htmlElement.classList.remove("star-wars-theme");

        // Stop the crawl animation
        crawl.classList.remove("active");
    });

    starWarsButton.addEventListener("click", function () {
        // Remove disco effect
        header.classList.remove("disco-active");
        buttons.forEach(button => {
            button.classList.remove("disco-active");
        });

        // Apply Star Wars theme
        htmlElement.classList.add("star-wars-theme");

        // Start the crawl animation
        crawl.classList.add("active");
    });
});
