def print_menu(menu):
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**                                **")
    print("** To quit at any time, type 'quit' **")
    print("**************************************")
    for category, items in menu.items():
        print(f"\n{category}\n----------")
        for item in items:
            print(item)
    print("\n***********************************")
    print("** What would you like to order? **")
    print("***********************************")

def add_to_order(order, user_order):
    if user_order.lower() == 'quit':
        print("Exiting")
        return False
    if user_order in [item for sublist in restaurant_menu.values() for item in sublist]:
        order[user_order] = order.get(user_order, 0) + 1
        print(f"** {order[user_order]} order(s) of {user_order} has been added to your meal **")
    else:
        print(f"** We don't have {user_order} on the menu. Please choose something else. **")
    return True

def print_summary(order):
    print("***********************************")
    print("** Here is your complete order: **")
    print("***********************************")
    for item, count in order.items():
        print(f"{count} order(s) of {item}")
    print("***********************************\n")

def start_ordering(menu):
    order = {}
    print_menu(menu)
    while True:
        user_input = input("> ").strip().capitalize() #this is the character discussed in the lab requirements for input
        if not add_to_order(order, user_input):
            break
    print_summary(order)

if __name__ == "__main__":
    restaurant_menu = {
        "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
        "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
        "Desserts": ["Ice Cream", "Cake", "Pie"],
        "Drinks": ["Coffee", "Tea", "Unicorn Tears", "Beer"]
    }
    start_ordering(restaurant_menu)
