# Week 10 Prove: Assignment Milestone
# Shopping Cart
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse110-course/lesson09/prove.html

cart_list_names = []
cart_list_prices = []
keep_running = True
spaces = 10

# Function to print some decorative elements
def print_elements(option): 
    break_line = "\n***********************************************\n"
    section_line = "***********************************************"
    header       = "*   Welcome to the Shopping Cart Program!     *"
    footer       = "*  Thanks for use the Shopping Cart Program!  *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")
    elif option == "break_line":
        print(f"{break_line}")
    elif option == "section_line":
        print(f"{section_line}")

# Function to show the menu items
def show_menu():
    action = 0
    
    print(
        "Please select one of the following: \n" \
        "1. Add item\n" \
        "2. View cart\n" \
        "3. Remove item\n" \
        "4. Compute total\n" \
        "5. Quit\n" \
    )

    # To prevent invalid entries
    while action not in range(1, 6):
        # To prevent non numeric entries
        try:
            action = int(input("Please enter an action: ") or 0)
        except:
            action = 0

    return action

# Function of Action 1. Add item
def add_item():
    global spaces
    item_name = ""
    item_price = 0

    # To prevent empty entries
    while item_name == "":
        item_name = input("\nWhat item would you like to add? ").capitalize().strip()

    # To prevent empty/zero/non numeric prices
    while item_price == 0:
        try:
            item_price = float(input(f"What is the price of '{item_name}'? ") or 0)
        except:
            item_price = 0
    
    # Adding the item and price into cart list
    cart_list_names.append(item_name)
    cart_list_prices.append(item_price)    
    print(f"'{item_name}' has been added to the cart.")
    print_elements("break_line")
    
    if spaces < len(item_name):
        spaces = len(item_name) + 1

# Function of Action 2. View cart
def view_cart():

    # To validate if the list has any entry
    if cart_list_names:
        print("\nThe contents of the shopping cart are:")
        for i, (name, price) in enumerate(zip(cart_list_names, cart_list_prices)):
            print(f"{(i + 1):2d}. {name:<{spaces}} - ${price:6.2f}")
    else:
        print("\nYour cart is empty.")
    print_elements("break_line")

# Function of Action 3. Remove item
def remove_item():
    # To validate if the list has any entry
    if cart_list_names:
        
        # To prevent non numeric item
        try: 
            index = int(input("\nWhich item would you like to remove? ")) - 1
            
            if index in range(len(cart_list_names)):
                # Removing the item and price from cart list
                cart_list_names.pop(index)
                cart_list_prices.pop(index)
                print("\nItem removed.")
            else:
                print("\nSorry, that is not a valid item number.")
        except:
            print("\nSorry, that is not a valid item number!")
    else:
        print("\nYour cart is empty.")
    print_elements("break_line")    

# Function of Action 4. Compute total
def compute_total():
    print(f"\nThe total price of the items in the shopping cart is ${sum(cart_list_prices):.2f}")
    print_elements("break_line")

# Function of Action 5. Quit
def quit():
    print_elements("footer")
    return False

# Starting to run the program
print_elements("header")

while keep_running:
    action = show_menu()

    if action == 1:
        add_item()
    elif action == 2:
        view_cart()
    elif action == 3:
        remove_item()
    elif action == 4:
        compute_total()
    elif action == 5:
        keep_running = quit()