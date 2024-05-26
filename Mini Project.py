menu = {
    "Tea": 25,
    "Coffee": 25,
    "Veg Momo": 30,
    "Paneer Momo": 35,
    "Nonveg Momo": 40,
    "Veg Burger": 50,
    "Nonveg Burger": 65,
    "Noodle": 60,
    "Pizza": 80,
    "Pasta": 120,
}

def display_menu(menu):
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

def take_order(menu):
    order = {}
    while True:
        item = input("Enter the item you want to order (or type 'done' to finish): ")
        if item.lower() == 'done':
            break
        elif item not in menu:
            print(f"Sorry, we don't have {item}. Please choose from the menu.")
        else:
            quantity = int(input(f"How many {item}s would you like to order? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
    return order

def calculate_total(order, menu):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

def main():
    display_menu(menu)
    order = take_order(menu)
    total = calculate_total(order, menu)
    print("\nYour order:")
    for item, quantity in order.items():
        print(f"{item}: {quantity} x ${menu[item]} = ${menu[item] * quantity}")
    print(f"\nTotal: ${total}")

if __name__ == "__main__":
    main()