# menu.py
# This file contains the restaurant menu and functions
# related to displaying and managing menu items.

# Restaurant menu stored using a dictionary
MENU = {
    1: {"name": "Chicken Rice", "price": 6.50},
    2: {"name": "Nasi Goreng", "price": 7.00},
    3: {"name": "Fried Mee", "price": 6.00},
    4: {"name": "Fish and Chips", "price": 12.00},
    5: {"name": "Vegetable Burger", "price": 8.50},
    6: {"name": "French Fries", "price": 4.00},
    7: {"name": "Iced Milo", "price": 3.50},
    8: {"name": "Orange Juice", "price": 4.00}
}


def display_menu():
    """Display all available food and drink items."""
    print("\n========== RESTAURANT MENU ==========")
    print(f"{'No.':<5}{'Item':<20}{'Price (RM)':>10}")
    print("--------------------------------------")

    for number, item in MENU.items():
        print(f"{number:<5}{item['name']:<20}{item['price']:>10.2f}")

    print("======================================")


def get_menu_item(item_number):
    """Return a menu item using its item number."""
    return MENU.get(item_number)


def is_valid_item(item_number):
    """Check whether an item number exists in the menu."""
    return item_number in MENU
