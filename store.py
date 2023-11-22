Aisles = [
         "Fruits (1)",
         "Frozen (2)",
         "Seafood (3)"]
Items = [[
         "fruit 1",
         "fruit 2",
         "fruit 3",],
         [
         "frozen 1",
         "frozen 2",
         "frozen 3",],
         [
         "seafood 1",
         "seafood 2",
         "seafood 3"]]
Options = [
    "Aisles (1)",
    "Current items (2)",
    "Proceed to checkout (3)"
]
user_cart = []
scanned_item_list= []

# STAGE 1: AISLE AND ITEM SELECTION

# greets the user and gets their input for their aisle choice
def get_aisle_choice():
    aisle_input = int(input(f"Welcome to Sinn Cafe! here are the available aisles:\n" + "\n".join(Aisles) + "\n\nPlease enter the aisle number: "))
    return aisle_input
aisle_choice = get_aisle_choice()
# gets the user input on item choice
def get_item_choice():
    return int(input(f"Available Items:\n" + "\n".join(Items[aisle_choice - 1]) + "\n\nPlease select an item: "))
# gets the user input on returning to previous sections or progressing to checkout
def display_options():
    return int(input(f"please select another aisle, item or proceed to checkout: "))

# if the user aisle choice is in range of list of aisle, it displays their choice and progresses to items
if 1 <= aisle_choice <= len(Aisles):
    print("You've chosen: " + Aisles[aisle_choice - 1])
# asks for user item choice within range of respective aisle list and adds the item(s) to the user cart list
    while True:
        item_choice = get_item_choice()

        if 1 <= item_choice <= len(Items[aisle_choice - 1]):
            chosen_item = Items[aisle_choice - 1][item_choice - 1]
            user_cart.append(chosen_item)
            print("You've chosen: " + chosen_item)
        else:
            print("please enter a valid item number")

        print(Options)
        option_choice = display_options()

        if option_choice == 1:
            aisle_choice = get_aisle_choice()
        elif option_choice == 2:
            get_item_choice()
        elif option_choice == 3:
            print("Checkout complete. Items in your cart:")
            for item in user_cart:
                print("- " + item)
            break
        else:
            print("Please enter a valid option")

else:
     print("Please enter a valid aisle number")

# STAGE 2 Checkout and payment

scannable_item = user_cart[0]

if option_choice == 3:
  for item in user_cart:
    scan_prompt = input(f"Please scan {item} in cart to proceed(i.e. saying: scan): ")

    if scan_prompt == "scan":
      print(f"you scanned {item}")
      scanned_item_list.append(item)
      
    elif scan_prompt != "scan":
      print("please enter scan to proceed")
      break
    
  else:
      print(f"All items scanned.\n")
  
# STAGE 3: payment info
def expiration_func():
    max_month = 12
    min_year = 23
    
    while True:
        expiration_date = input("Enter the expiration date (MM/YY): ")
        
        if "/" in expiration_date:
            mm, yy = expiration_date.split("/")
            
            if 1 <= int(mm) <= max_month and mm.isdigit() and  int(yy) >= min_year <= 99:
                security_func()
                break
            else:
                print("Invalid expiration date. Please try again.")
        else:
            print("Invalid format. Please use MM/YY.")



def security_func():
    while True:
      security_number = input("Enter the security number: ")
  
      if len(security_number) != max_cvv_length or not security_number.isdigit():
        print("Invalid card number length or format. Please try again: ")
      else:
        print("payment successful!\n")
        for item in scanned_item_list:
          print("-" + item)
        break
max_card_length = 16
max_cvv_length = 3
while True:
    user_card_num = input("Please enter your card number for payment: ")

    if len(user_card_num) != max_card_length or not user_card_num.isdigit():
        print("Invalid card number length or format. Please try again.")
    else:
      expiration_func()
      break