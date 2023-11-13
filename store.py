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
# ScannedItems = []
# UserCart = []

# STAGE 1: AISLE AND ITEM SELECTION

# def DisplayItems():
# UserResponse2 = int(input(f"Available Items:\n" + "\n".join(Items[chosen_aisle]) + "\n\nPlease select an item: "))

UserResponse = int(input(
   f"Welcome to Sinn Cafe! here are the available aisles:\n" + "\n".join(Aisles) + "\n\nPlease enter the aisle number: "))

if 1 <= UserResponse <= len(Aisles):
    chosen_aisle = Aisles[UserResponse - 1]
    print("You've chosen: " + chosen_aisle)
    # Make if elifs into one interchangable func based on user input
    if UserResponse == 1:
        UserResponse2 = int(input(f"Available Items:\n" + "\n".join(Items[0]) + "\n\nPlease select an item: "))
    elif UserResponse == 2:
        UserResponse2 = int(input(f"Available Items:\n" + "\n".join(Items[1]) + "\n\nPlease select an item: "))
    elif UserResponse == 3:
        UserResponse2 = int(input(f"Available Items:\n" + "\n".join(Items[2]) + "\n\nPlease select an item: "))
else:
    print("Please enter a valid aisle number")

# fix chosen item not displaying properly
if 1 <= UserResponse2 <= len(Items[UserResponse - 1]):
   chosen_item = Items[UserResponse2 - 1]
   print("You've chosen ".join(chosen_item))