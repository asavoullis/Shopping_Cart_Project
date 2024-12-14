from ItemClass import Item
from datetime import datetime, timedelta
import pandas as pd


class Shop:
    """
    Represents a shop where customers can purchase items.
    """

    def __init__(self):
        """
        Initializes the shop with tax and an empty inventory.
        """
        self.tax_amount = 0.13  # Sales tax percentage
        self.available_items = []

    def add_available_items_from_file(self, input_filename):
        """
        Loads available items into the shop's inventory from a file.

        :param input_filename: Name of the input file (str).
        """
        with open(input_filename, "r") as input_file:
            for row in input_file:
                item_data = row.split()
                name, quantity, price = (
                    item_data[0],
                    int(item_data[1]),
                    float(item_data[2]),
                )
                self.available_items.append(Item(name, quantity, price))

    def show_available_items(self):
        """
        Prints all available items in the shop.
        """
        if not self.available_items:
            print("No items available in the shop.")
        else:
            print("Available Items:")
            for item in self.available_items:
                print(
                    f"Name: {item.name}, Quantity: {item.quantity}, Price: {item.price}"
                )

    def show_items_in_table(self):
        """
        Displays the available items in a table format using pandas.
        """
        if not self.available_items:
            print("No items available in the shop.")
            return

        data = [[item.name, item.quantity, item.price] for item in self.available_items]
        df = pd.DataFrame(data, columns=["Name", "Quantity", "Price"])
        print("*****************************************")
        print(df)
        print("*****************************************")

    def sell_items(self, item_name, quantity, customer):
        """
        Processes the sale of an item to a customer.

        :param item_name: Name of the item to sell (str).
        :param quantity: Quantity of the item to sell (int).
        :param customer: Customer object buying the item.
        """
        for item in self.available_items:
            if item.name == item_name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    sold_item = Item(item.name, quantity, item.price)
                    customer.add_item_into_items(sold_item)
                    print(f"Sold {quantity} of {item_name} to {customer.name}.")
                    return
                else:
                    print(
                        f"Not enough stock for {item_name}. Available: {item.quantity}"
                    )
                    return
        print(f"Item {item_name} not found in the shop.")

    def save_items_in_file(self, output_filename):
        """
        Saves the shop's inventory to a file.

        :param output_filename: Name of the output file (str).
        """
        with open(output_filename, "w") as output_file:
            for item in self.available_items:
                output_file.write(f"{item.name} {item.quantity} {item.price}\n")

    def get_order_pickup_time(self):
        """
        Calculates and returns the order pickup time as the current time + 1 hour.

        :return: Pickup time as a datetime object.
        """
        pickup_time = datetime.now() + timedelta(hours=1)
        print(
            f"Your order will be ready for pickup at: {pickup_time.strftime('%Y-%m-%d %H:%M:%S')}."
        )
        return pickup_time

    def show_welcome_message(self, customer):
        """
        Displays a personalized welcome message for the customer.

        :param customer: Customer object.
        """
        welcome_message = f"Welcome to our store, {customer.get_name().title()}!"
        print("*" * len(welcome_message))
        print(welcome_message)
        print("*" * len(welcome_message))
