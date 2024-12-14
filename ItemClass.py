class Item:
    """
    Represents an item in the shopping cart system.
    """

    def __init__(self, name, quantity, price):
        """
        Initializes a new item with its name, quantity, and price.

        :param name: Name of the item (str).
        :param quantity: Quantity of the item (int).
        :param price: Price of the item (float or str that can be converted to float).
        """
        self.name = name
        self.quantity = quantity
        self.price = float(price)  # Ensure price is stored as a float

    def __str__(self):
        """
        Returns a string representation of the item.

        :return: String with item details.
        """
        return (
            f"Item(Name: {self.name}, Quantity: {self.quantity}, Price: {self.price})"
        )

    def calculate_subtotal(self):
        """
        Calculates the subtotal for the item (quantity * price).

        :return: Subtotal as a float.
        """
        return self.quantity * self.price

    def get_name(self):
        """
        Retrieves the name of the item.

        :return: Name of the item (str).
        """
        return self.name

    def set_name(self, name):
        """
        Updates the name of the item.

        :param name: New name for the item (str).
        """
        self.name = name

    def get_quantity(self):
        """
        Retrieves the quantity of the item.

        :return: Quantity of the item (int).
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Updates the quantity of the item.

        :param quantity: New quantity for the item (int).
        """
        self.quantity = quantity

    def get_price(self):
        """
        Retrieves the price of the item.

        :return: Price of the item (float).
        """
        return self.price

    def set_price(self, price):
        """
        Updates the price of the item.

        :param price: New price for the item (float or str that can be converted to float).
        """
        self.price = float(price)
