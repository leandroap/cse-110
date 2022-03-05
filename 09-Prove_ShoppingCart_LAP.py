# Week 09 Prove: Assignment Milestone
# Shopping Cart
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse110-course/lesson09/prove.html

cart_list_names = []
cart_list_prices = []
keep_running = True

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

# Action: 1. Add item
def add_item():
    item_name = ""

    # To prevent empty entries
    while item_name == "":
        item_name = input("\nWhat item would you like to add? ").capitalize().strip()
    
    cart_list_names.append(item_name)
    print(f"'{item_name}' has been added to the cart.\n")

# Action: 2. View cart
def view_cart():

    # To validate if the list has any entry
    if cart_list_names:
        print("\nThe contents of the shopping cart are:")
        
        for i, name in enumerate(cart_list_names):
            print(f"{i+1}. {name}")
        print_elements("section_line")
    else:
        print("\nYour cart is empty.")
    print()

# Action: 3. Remove item
def remove_item():
    print("\n#TODO\n")

# Action: 4. Compute total
def compute_total():
    print("\n#TODO\n")

# Action: 5. Quit
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