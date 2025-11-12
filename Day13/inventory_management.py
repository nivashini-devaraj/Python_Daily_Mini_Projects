class Store:
    def __init__(self):
        # Encapsulation: Private attributes
        self.__products = []       # List of product dictionaries
        self.__total_earnings = 0  # Private variable for total earnings

    # Abstraction: Public method to add products
    def add_product(self, name, price, quantity):
        product = {"name": name, "price": price, "quantity": quantity}
        self.__products.append(product)
        print(f" Product '{name}' added successfully!")

    # Abstraction: Public method to display products
    def show_products(self):
        if not self.__products:
            print("No products available.")
        else:
            print("\n Available Products:")
            for item in self.__products:
                print(f"{item['name']} - ${item['price']} | Quantity: {item['quantity']}")
            print(f"\n Total Earnings: ${self.__total_earnings}\n")

    # Getters (to safely access private data)
    def get_products(self):
        return self.__products

    def get_earnings(self):
        return self.__total_earnings

    # Protected method (for use in subclasses)
    def _update_earnings(self, amount):
        self.__total_earnings += amount


# Derived Class (Method Overriding)
class Customer(Store):
    def __init__(self):
        super().__init__()  

    # Override buy_product method
    def buy_product(self, product_name, quantity):
        products = self.get_products()
        for item in products:
            if item["name"].lower() == product_name.lower():
                if item["quantity"] >= quantity:
                    item["quantity"] -= quantity
                    cost = item["price"] * quantity
                    self._update_earnings(cost)
                    print(f" Purchased {quantity} of '{item['name']}' for ${cost}")
                else:
                    print(f" Only {item['quantity']} '{item['name']}' left in stock.")
                break
        else:
            print(f" Product '{product_name}' not found.")


# --- Example Use ---
store = Customer()

# Add products
store.add_product("Apple", 2, 50)
store.add_product("Banana", 1, 100)
store.add_product("Milk", 3, 30)

# Show available stock
store.show_products()

# Buy some products
store.buy_product("Apple", 5)
store.buy_product("Milk", 2)

# Show updated stock
store.show_products()
