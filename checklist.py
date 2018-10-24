# coding: utf8
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
        # printing all items in yellow
        print("\033[33m" + "{} {}".format(index, list_item))
        index += 1

# function that marks items in the list as completed
def mark_completed(index):
    # marked items are printed in green
    print("\033[32m" + "{} {}".format("√", read(index)))

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

    # CREATE ITEM
    if function_code == "C":
        input_item = user_input("Input item to the list: ")
        create(input_item)
        print(input_item + " is added to the list")

    # READ ITEM
    elif function_code == "R":
        item_index = int(user_input("Insert Index Number of an Item to be printed: "))
        # Remember that item_index must actually exist or our program will crash.
        if checklist == list():
            # error printed in red
            print('\033[31m' + "The list is empty")
            running = True
        else:
            print(read(item_index))

    # PRINTINT THE LIST
    elif function_code == "P":
        if checklist == list():
            # error printed in red
            print('\033[31m' + "The list is empty")
            running = True
        else:
            print("The following items are in the list:")
            list_all_items()

    # MARK AS COMPLETED
    elif function_code == "M":
        marked_item = int(user_input(
            "Insert Index of an Item to be marked as completed: "))
        mark_completed(marked_item)
    
    # UPDATING THE LIST
    # elif function_code == "U":
    #      item_index = int(user_input("Insert Index Number of an Item to be printed: "))

    # DELETE ITEM 
    elif function_code == "D":
        del_item = int(user_input("Insert Index of an Item to delete: "))

        if checklist == list():
            # error printed in red
            print('\033[31m' + "The list is empty")
            running = True
        else:
            # message printed in green
            print('\033[32m' + read(int(del_item)) + " - deleted now")
            destroy(del_item)


    elif function_code == "Q":
        # This is where we want to stop our loop
        return running

    # Catch all
    else:
        # error message is printed in magenta
        print('\033[35m' + "Unknown Option")
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
    selection = user_input("\033[0m" +
                           "Press C to add to list, R to Read from list, P to print the full list, M to mark as completed, D to delete an item and Q to quit >>> ")
    running = select(selection)

