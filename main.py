from datetime import datetime, timedelta
from ShopClass import Shop
from ItemClass import Item
from CustomerClass import Customer
import pandas as pd


def main():
    """
    Main function to simulate the shopping system.
    """
    # Initialize the shop and load available items
    shop = Shop()
    shop.add_available_items_from_file("available_grocery_items.txt")

    # Collect customer details and create a customer
    while True:
        user_name = input("Please enter your name: ").title()
        if user_name.strip():
            customer = Customer(
                customer_id=1, name=user_name, email=f"{user_name.lower()}@example.com"
            )
            shop.show_welcome_message(customer)
            break

    input("Press enter to continue...")
    print("*******************************************")
    shop.show_items_in_table()
    print("*******************************************")

    # Simulate shopping process
    while True:
        item_added = input("Add an item: ").title()
        available = False
        for item in shop.available_items:
            if item.get_name() == item_added:
                while True:
                    try:
                        item_qty = int(input("Add quantity: "))
                        break
                    except ValueError:
                        print("Quantity should be in digits!")

                try:
                    shop.sell_items(item_added, item_qty, customer)
                    available = True
                    break
                except ValueError:
                    print(
                        "The store does not have enough stock of the selected product."
                    )
                    continue
        if not available:
            print("The product is not available in the store.")

        proceed_shopping = input("Do you wish to add more items? (yes/no): ")
        if proceed_shopping.lower() != "yes":
            break
        else:
            shop.show_items_in_table()

    # Generate and display bill summary
    order_date_time = datetime.now().strftime("%B %d, %Y %I:%M:%S %p")
    order_pickup_time = (datetime.now() + timedelta(hours=2)).strftime("%I:%M %p")
    total_with_tax = customer.total + (customer.total * shop.tax_amount)

    customer.save_items_in_file("Cart.txt")

    print("\n")
    print(" Bill Summary ".center(41, "*"))
    print("Order Date & Time:", order_date_time)
    print("\n")

    with open("Cart.txt", "r") as cr:
        df = pd.read_csv(
            "Cart.txt", sep=" ", header=None, names=["Items", "Quantity", "Sub Total"]
        )
        print("*****************************************")
        print(df)
        print("*****************************************")
        cr.close()

    print(f"Your total bill (including 13% tax) is: ${total_with_tax:.2f}!")
    print("\n")
    print("Your order will be ready to pick up in two hours.")
    print("\n")
    print(
        f"{customer.get_name()}, you can pick up your order after {order_pickup_time}!"
    )
    print("\n")
    print(" Thank You ".center(41, "*"))
    print("\n")
    print("Hope to see you back soon!")


if __name__ == "__main__":
    main()
