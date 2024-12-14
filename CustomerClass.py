class Customer:
    """
    Represents a customer in the shopping cart system.
    """

    def __init__(self, customer_id, name, email):
        """
        Initializes a new customer with their ID, name, and email.

        :param customer_id: Unique identifier for the customer (int or str).
        :param name: Name of the customer (str).
        :param email: Email address of the customer (str).
        """
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.cart = []  # Initialize an empty shopping cart
        self.items = []  # Initialize an empty list for items
        self.total = 0.0  # Initialize total cost

    def get_name(self):
        """
        Retrieves the name of the customer.

        :return: Name of the customer (str).
        """
        return self.name

    def set_name(self, name):
        """
        Updates the name of the customer.

        :param name: New name for the customer (str).
        """
        self.name = name

    def add_to_cart(self, item):
        """
        Adds an item to the customer's shopping cart.

        :param item: Item to be added (can be a dictionary or an object).
        """
        self.cart.append(item)

    def remove_from_cart(self, item):
        """
        Removes an item from the customer's shopping cart if it exists.

        :param item: Item to be removed (can be a dictionary or an object).
        """
        if item in self.cart:
            self.cart.remove(item)

    def view_cart(self):
        """
        Returns the current contents of the shopping cart.

        :return: List of items in the cart.
        """
        return self.cart

    def add_item_into_items(self, item):
        """
        Adds an item to the list of items and updates the total cost.

        :param item: Item object with name, quantity, and price attributes.
        """
        self.items.append(item)
        self.total += float(item.price) * int(item.quantity)

    def show_customer_items(self):
        """
        Displays the details of all items in the items list.

        :return: String representation of item details.
        """
        return "\n".join(
            f"Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}"
            for item in self.items
        )

    def save_items_in_file(self, output_filename):
        """
        Saves the details of all items to a file, including the subtotal for each item.

        :param output_filename: Name of the output file where items will be saved (str).
        """
        with open(output_filename, "w") as output_file:
            for item in self.items:
                subtotal = int(item.quantity) * float(item.price)
                output_file.write(
                    " ".join([item.name, str(item.quantity), str(subtotal)])
                )
                output_file.write("\n")

    def __str__(self):
        """
        Returns a string representation of the customer.

        :return: String with customer details.
        """
        return f"Customer({self.customer_id}, {self.name}, {self.email})"
