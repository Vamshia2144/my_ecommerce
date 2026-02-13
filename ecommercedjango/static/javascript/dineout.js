document.addEventListener("DOMContentLoaded", function () {
    // Select all "Book Now" buttons
    let bookButtons = document.querySelectorAll(".book-btn");

    bookButtons.forEach(button => {
        button.addEventListener("click", function () {
            // Get the restaurant name from the nearest figcaption
            let restaurantName = this.parentElement.querySelector("figcaption").textContent;

            // Show an alert message with the restaurant name
            alert(`${restaurantName} has been booked successfully!`);
        });
    });
});
