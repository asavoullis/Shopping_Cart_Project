# Shopping Cart System

## Overview
This project implements a simple shopping cart system using Object-Oriented Programming (OOP) in Python. It includes functionalities to manage a shop, handle customer purchases, and maintain inventory.

---

## Files and Their Purpose

### 1. `main.py`
- **Purpose:** The entry point of the application.
- **Description:**
  - Initializes the shop and loads inventory from `available_grocery_items.txt`.
  - Collects customer details and handles shopping interactions.
  - Generates a bill summary and saves customer receipts in `Cart.txt`.
  - Displays the order pickup time and provides a thank-you message to the customer.

### 2. `ShopClass.py`
- **Purpose:** Contains the `Shop` class that manages the shop's inventory and operations.
- **Key Features:**
  - Load items from a file into inventory.
  - Display available items in a table format.
  - Handle item sales to customers.
  - Save updated inventory to a file.
  - Calculate order pickup times.
  
### 3. `CustomerClass.py`
- **Purpose:** Defines the `Customer` class, which represents a customer.
- **Key Features:**
  - Maintain customer details such as name, email, and shopping cart.
  - Manage items added to the cart.
  - Generate a receipt and save it to a file.

### 4. `ItemClass.py`
- **Purpose:** Implements the `Item` class for representing individual items in the shop.
- **Key Features:**
  - Store details like name, quantity, and price.
  - Calculate the subtotal for an item based on quantity and price.

### 5. `requirements.txt`
- **Purpose:** Lists the dependencies required to run the project.
- **Content:**
  - `pandas`: Used for tabular display of data.
  - `python>=3.10`: Specifies the required Python version.

### 6. `available_grocery_items.txt`
- **Purpose:** A sample inventory file containing available items.
- **Content Format:**
  - Each line specifies an item, its quantity, and price.
  - Example:
    ```
    Apple 100 1.2
    Banana 150 0.5
    ```

### 7. `Cart.txt`
- **Purpose:** Auto-generated during program execution to store the customer's purchased items and their subtotals.
- **Content Format:**
  - Each line specifies an item, its quantity, and subtotal.
  - Example:
    ```
    Apple 2 2.4
    Banana 3 1.5
    ```

---

## How the Code Works

### Step 1: Load the Shop Inventory
The program reads the inventory data from `available_grocery_items.txt` and loads it into the shop object using the `add_available_items_from_file` method in `ShopClass`.

### Step 2: Customer Interaction
1. The program prompts the user to enter their name, creating a `Customer` object.
2. A personalized welcome message is displayed.

### Step 3: Shopping Process
1. The user can view available items in the shop.
2. The user adds items to their cart by specifying the item name and quantity.
3. The shop verifies the availability of the item and updates the inventory.

### Step 4: Bill Summary
1. The program calculates the total bill, including tax.
2. The bill summary is displayed in tabular format using `pandas`.
3. The program saves the customer’s receipt to `Cart.txt`.

### Step 5: Order Pickup
The program calculates the pickup time (current time + 2 hours) and displays it to the customer.

---

## How to Run the Project
1. Ensure Python 3.10 or above is installed.
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Place `available_grocery_items.txt` in the same directory as the code.
4. Run the program:
   ```bash
   python main.py
   ```

---

## Future Enhancements
- Add support for dynamic tax rates.
- Implement user authentication for multiple customers.
- Save and load previous customer orders.
- Add more detailed exception handling for robust error management.

---

## Acknowledgments
This project demonstrates the application of OOP principles and Python programming to create a practical shopping system.

