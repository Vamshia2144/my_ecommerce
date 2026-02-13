// Get all "Add to Cart" buttons
let cartButtons = document.querySelectorAll(".cart-btn");

cartButtons.forEach(button => {
    button.addEventListener("click", function () {
        let foodItem = this.parentElement; // Get the parent div
        let foodImage = foodItem.querySelector("img").src; // Get food image
        let foodName = foodItem.querySelector("figcaption").textContent; // Get food name
        let foodPrice = foodItem.querySelector(".price").textContent; // Get price

        // Create an object for the selected food
        let cartItem = {
            image: foodImage,
            name: foodName,
            price: foodPrice
        };

        // Get existing cart data from localStorage
        let cart = JSON.parse(localStorage.getItem("cart")) || [];

        // Add new item to cart
        cart.push(cartItem);

        // Save updated cart data to localStorage
        localStorage.setItem("cart", JSON.stringify(cart));

        alert(foodName + " added to cart!");
    });
});