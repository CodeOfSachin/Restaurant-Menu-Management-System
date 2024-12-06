def read_menu_file(file_name):  
    with open(file_name, "r") as menu_file:
            lines = menu_file.readlines()
         
    menu_items = []
    MENU_LINE_INTERVAL = 2
    for i in range(0, len(lines), MENU_LINE_INTERVAL):
        name = lines[i].strip()
        price = float(lines[i+1].strip())
        menu_items.append((name, price))
    return menu_items

def display_menu(menu_title, menu_items):
    print(f"{menu_title:^45}")
    print(f"{'Item':<30}{'Price':>12}")
    print("-" * 45)
    item_id = 1
    for item, price in menu_items:
        print(f"{item_id}. {item:<26}{'Rs':>5}{price:>10.2f}")
        item_id = item_id + 1
    print("-" * 45)
    print("")

def take_order(menu_title, menu_items):
    order = []
    total_cost = 0
    while True:
        item_number = int(input(f"Enter a id of {menu_title} you want to order (0 for exit)"))
        if item_number == 0:
            break
        elif  0 < item_number  <= len(menu_items):
            item_name, item_price = menu_items[item_number - 1]
            quantity = int(input(f"How many {item_name}s would you like to order?: "))
            if quantity > 0:
                order.append((item_name, item_price, quantity))
                print(f"{quantity} {item_name} added")
            else:
                print("Quantity must be greater than 0")
        else:
            print(f"Invalid {menu_title} id. Please try again")
    return order

def all_order_records(food_order, drink_order):
    total_order = food_order + drink_order
    return total_order

def total_cost(total_order):
    overall_cost = float(sum(price * quantity for _, price, quantity in total_order))
    return overall_cost

def order_receipt(total_order, overall_cost):
    print(f"{'Order Receipt':^60}")
    print(f"{'Item':<30}{'Price':>15}{'Quantity':>10}")
    print("-" * 60)
    item_id = 1
    for item, price, quantity in total_order:
        print(f"{item_id}. {item:<26}{'Rs':>5}{price:>10.2f}{quantity:>10}")
        item_id = item_id + 1
    print("-" * 60)
    print(f"{'Total':>45}{overall_cost:>10.2f}")
    print("")

FOOD_MENU_FILE = "food_menu.txt"
DRINK_MENU_FILE = "drink_menu.txt"
food_menu_items = read_menu_file(FOOD_MENU_FILE)
drink_menu_items = read_menu_file(DRINK_MENU_FILE)
food_menu = display_menu("FOODS", food_menu_items)
drink_menu = display_menu("DRINKS", drink_menu_items)
food_order = take_order("Food", food_menu_items)
drink_order = take_order("Drink", drink_menu_items)
full_order = all_order_records(food_order, drink_order)
total = total_cost(full_order)
order_receipt(full_order, total)

