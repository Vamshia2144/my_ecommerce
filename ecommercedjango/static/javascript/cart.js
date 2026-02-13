document.addEventListener("DOMContentLoaded", function () {
    let cartContainer = document.getElementById("cart-items");
    let totalPriceElement = document.createElement("p");
    totalPriceElement.id = "total-price";
    cartContainer.appendChild(totalPriceElement);

    // Get cart data from localStorage
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    let totalAmount = 0;

    if (cart.length === 0) {
        cartContainer.innerHTML = "<p>Your cart is empty!</p>";
    } else {
        cart.forEach((item, index) => {
            let itemDiv = document.createElement("div");
            itemDiv.innerHTML = `
                <img src="${item.image}" width="220" height="220">
                <span>${item.name}</span>
                <span>${item.price}</span>
                <button onclick="removeItem(${index})">Remove</button>
                <hr>
            `;

            // Extract numeric value from price
            let price = parseInt(item.price.replace("Rs.", "").replace("/-", "").trim());
            totalAmount += price; // Add to total

            cartContainer.appendChild(itemDiv);
        });

        // Display total price
        totalPriceElement.textContent = `Total: Rs.${totalAmount}/-`;
        
        // Add checkout button
        let checkoutButton = document.createElement("button");
        checkoutButton.textContent = "Proceed to Payment";
        checkoutButton.id = "checkout-btn";
        checkoutButton.onclick = function () {
            alert(`Proceeding to payment. Total Amount: Rs.${totalAmount}/-`);
        };

        cartContainer.appendChild(checkoutButton);
    }
});

function removeItem(index) {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];
    cart.splice(index, 1); // Remove the selected item
    localStorage.setItem("cart", JSON.stringify(cart));
    location.reload(); // Refresh page to update cart
}

function clearCart() {
    localStorage.removeItem("cart");
    location.reload();
}
