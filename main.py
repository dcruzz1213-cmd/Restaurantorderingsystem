# main.py
# Restaurant Ordering System
# This program allows customers to view the menu,
# place orders, view their order and calculate the bill.

from menu import display_menu, get_menu_item, is_valid_item


# Store the customer's order
order = {}


def add_to_order():
    """Allow the customer to select an item and quantity."""

    display_menu()

    try:
        item_number = int(input("Enter the item number: "))

        # Check whether the selected item exists
        if not is_valid_item(item_number):
            print("Invalid item number. Please try again.")
            return

        quantity = int(input("Enter quantity: "))

        # Validate quantity
        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        # Add item to the order
        if item_number in order:
            order[item_number] += quantity
        else:
            order[item_number] = quantity

        item = get_menu_item(item_number)

        print(
            f"{quantity} x {item['name']} "
            f"added to your order successfully!"
        )

    except ValueError:
        print("Invalid input. Please enter numbers only.")


def view_order():
    """Display all items currently in the customer's order."""

    if not order:
        print("\nYour order is currently empty.")
        return

    print("\n========== YOUR ORDER ==========")

    total = 0

    for item_number, quantity in order.items():
        item = get_menu_item(item_number)

        subtotal = item["price"] * quantity
        total += subtotal

        print(
            f"{item['name']:<20} "
            f"x {quantity:<3} "
            f"RM {subtotal:.2f}"
        )

    print("--------------------------------")
    print(f"Current Total: RM {total:.2f}")
    print("================================")


def calculate_bill():
    """Calculate and display the final bill."""

    if not order:
        print("\nYou have not ordered anything yet.")
        return

    total = 0

    print("\n========== FINAL BILL ==========")

    for item_number, quantity in order.items():
        item = get_menu_item(item_number)

        subtotal = item["price"] * quantity
        total += subtotal

        print(
            f"{item['name']:<20} "
            f"x {quantity:<3} "
            f"RM {subtotal:.2f}"
        )

    # Give a discount when the total is RM50 or more
    discount = 0

    if total >= 50:
        discount = total * 0.10
        print(f"\nDiscount (10%): RM {discount:.2f}")

    final_total = total - discount

    print("--------------------------------")
    print(f"Subtotal:        RM {total:.2f}")
    print(f"Final Total:     RM {final_total:.2f}")
    print("================================")


def clear_order():
    """Remove all items from the current order."""

    if not order:
        print("\nThere is no order to clear.")
        return

    order.clear()
    print("\nYour order has been cleared successfully.")


def display_main_menu():
    """Display the main system menu."""

    print("\n")
    print("========================================")
    print("      RESTAURANT ORDERING SYSTEM")
    print("========================================")
    print("1. View Restaurant Menu")
    print("2. Add Item to Order")
    print("3. View Current Order")
    print("4. Calculate Final Bill")
    print("5. Clear Order")
    print("6. Exit")
    print("========================================")


def main():
    """Main function that controls the program."""

    while True:

        display_main_menu()

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                display_menu()

            elif choice == 2:
                add_to_order()

            elif choice == 3:
                view_order()

            elif choice == 4:
                calculate_bill()

            elif choice == 5:
                clear_order()

            elif choice == 6:
                print("\nThank you for using the Restaurant Ordering System!")
                print("Have a great day!")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")


# Start the program
if __name__ == "__main__":
    main()
