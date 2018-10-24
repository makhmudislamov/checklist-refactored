# creating empty array named checklist
checklist = []

# function that adds item to out checklist array - C of CRUD
def create(item):
    checklist.append(item)

# reading from the list - R of CRUD
def read(index):
    return checklist[index]

# updating item in the list = U of CRUD
def update(index, item):
    # example: checklist[1] = "Test" >> updates item in index=1 with string "Test" 
    checklist[index] = item

# deleting items from the checklist - D of CRUD
def destroy(index):
    checklist.pop(index)

# printing all items in the list
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# function that marks items in the list as completed
def mark_completed(index):
    print("{} {}".format("√", read(index)))

# unmarks the marked item from the list
def uncheck_item(index):
    mark_completed(index)
    print("{} {}".format("√", mark_completed(index)))

# function that takes input from users
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

# Select function that allows user to CRUD the checklist
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number?"))
        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        # This is where we want to stop our loop
        running = False
        return running

    # Catch all
    else:
        print("Unknown Option")
    return True

# testing all CRUD functions
# def test():
#     create("purple sox")
#     create("red cloak")

#     print(read(0))
#     print(read(1))

#     update(0, "purple socks")
#     destroy(1)

#     print(read(0))
#     list_all_items()
#     mark_completed(0)

#     user_value = user_input("Please Enter a value:")
#     print(user_value)

#     select("C")
#     list_all_items()

#     select("R")
#     list_all_items()

# test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to Read from list and P to display list")
    select(selection)

