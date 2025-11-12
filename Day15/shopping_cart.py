# Custom Exception for Out of Stock
class OutOfStockError(Exception):
    def __init__(self, message="Insufficient stock for the selected product."):
        self.message = message
        super().__init__(self.message)


# Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        # Available products in the store (product_name: [price, stock])
        self.store = {
            "Apple": [50, 10],
            "Banana": [10, 20],
            "Orange": [30, 15],
            "Mango": [60, 5]
        }
        self.cart = {}

    # Display available products
    def show_products(self):
        print("\nAvailable Products:")
        print("Product\tPrice\tStock")
        for item, (price, stock) in self.store.items():
            print(f"{item}\t{price}\t{stock}")

    # Add product to cart
    def add_to_cart(self, product, quantity):
        try:
            if product not in self.store:
                raise KeyError("Product not available in store.")

            quantity = int(quantity)
            if quantity <= 0:
                raise ValueError("Quantity must be positive.")

            if quantity > self.store[product][1]:
                raise OutOfStockError()

            # Add to cart and reduce store stock
            self.store[product][1] -= quantity
            if product in self.cart:
                self.cart[product] += quantity
            else:
                self.cart[product] = quantity

            print(f"Added {quantity} {product}(s) to your cart.")

        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        except OutOfStockError as e:
            print(e)

    # Remove product from cart
    def remove_from_cart(self, product):
        if product in self.cart:
            quantity = self.cart[product]
            del self.cart[product]
            # Return stock back to store
            self.store[product][1] += quantity
            print(f"Removed {product} from your cart.")
        else:
            print("Product not found in your cart.")

    # View items in cart
    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\nYour Cart:")
            print("Product\tQuantity\tPrice")
            total = 0
            for product, quantity in self.cart.items():
                price = self.store[product][0] * quantity
                total += price
                print(f"{product}\t{quantity}\t\t{price}")
            print(f"Total Amount: Rs.{total}")

    # Checkout and make payment
    def checkout(self):
        if not self.cart:
            print("Your cart is empty. Add items before checkout.")
            return

        total_amount = sum(self.store[item][0] * qty for item, qty in self.cart.items())
        print(f"\nYour total bill is Rs.{total_amount}")
        try:
            payment = float(input("Enter payment amount: "))
            if payment < total_amount:
                raise ValueError("Insufficient payment amount.")
            elif payment < 0:
                raise ValueError("Payment cannot be negative.")
            print(f"Payment successful! Change: Rs.{payment - total_amount:.2f}")
            print("Thank you for shopping with us!")
            self.cart.clear()
        except ValueError as e:
            print(e)


# --- Main Program ---
def main():
    cart = ShoppingCart()

    while True:
        print("\n===== ONLINE SHOPPING MENU =====")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cart.show_products()

        elif choice == "2":
            product = input("Enter product name: ").title()
            quantity = input("Enter quantity: ")
            cart.add_to_cart(product, quantity)

        elif choice == "3":
            product = input("Enter product name to remove: ").title()
            cart.remove_from_cart(product)

        elif choice == "4":
            cart.view_cart()

        elif choice == "5":
            cart.checkout()

        elif choice == "6":
            print("Exiting... ")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
