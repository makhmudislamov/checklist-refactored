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
    item = read(index)
    update(index, "√ " + item)
    print("\033[32m" + "{} {}".format("√", item))

# unmarks the marked item from the list
def uncheck_item(index):
    unmark = read(index)
    update(index, unmark)
    # print("\033[32m" + "{}" "{}".format(unmark, " - unmarked"))
    if "√" in checklist[index]:
        checklist[index].pop("√")


# function that takes input from users
def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

# SELECT FUNCTION that allows user to CRUD the checklist
def select(function_code):
    
    # CREATE ITEM
    # python trick using in and array. 
    # another option >> function_code == "C" or function_code == "c"
    # another option >> function_code.lower() makes all inputs lowercase.
    if function_code in ["C", "c"]:
        input_item = user_input("Input item to the list: ")
        print('\033[32m' + input_item + " - added to the list")
        create(input_item)
        

    # READ ITEM
    elif function_code in ["R", "r"]:
        item_index = int(user_input("Insert Index Number of an Item to be printed: "))
        # Remember that item_index must actually exist or our program will crash.
        if checklist == []:
            # error printed in red
            print('\033[31m' + "The list is empty")
            # running = True
        elif item_index in range(0, len(checklist)):
            print(read(item_index))
        else:
            print('\033[31m' + "Your input is out of range")

    # PRINTING THE LIST
    elif function_code in ["P", "p"]:
        if checklist == []:
            # error printed in red
            print("\033[31m" + "The list is empty")
            # running = True
        else:
            print("\033[33m" + "The following items are in the list:")
            list_all_items()

    # MARK AS COMPLETED
    elif function_code in ["M", "m"]:
        marked_item = int(user_input(
            "Insert Index of an Item to be marked as completed: "))
        if checklist == []:
            # error printed in red
            print('\033[31m' + "The list is empty")
        elif marked_item in range(0, len(checklist)):
            mark_completed(marked_item)
        else:
            print('\033[31m' + "Your input is out of range")

    # elif function_code in ["N", "n"]:
    #     unmark_item = int(user_input("Insert Index of an Item to uncheck :"))
    #     uncheck_item(unmark_item)
        
    
    # UPDATING THE LIST
    elif function_code in ["U", "u"]:
         item_index = int(user_input("Insert Index Number of an Item to update: "))
         item_name = user_input("Insert the item name: ")
         print("\033[32m" + item_name + " is added as an update")
         update(item_index, item_name)
      
    # DELETE ITEM 
    elif function_code in ["D", "d"]:
        del_item = int(user_input("Insert Index of an Item to delete: "))

        if checklist == []:
            # error printed in red
            print("\033[31m" + "The list is empty")
            # running = True
        elif del_item in range(0, len(checklist)):
             # message printed in green
            print("\033[32m" + read(int(del_item)) + " - deleted now")
            destroy(del_item)
        else:
            print('\033[31m' + "Your input is out of range")

    elif function_code in ["Q", "q"]:
        # This is where we want to stop our loop
        print('\033[32m' + "Bye Bye!")
        return False

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
    """Press:
        C to add to list, 
        R to Read from list, 
        P to print the full list, 
        U to update the list, 
        M to mark as completed, 
        D to delete an item,
        and Q to quit >> """)
    running = select(selection)

# ISSUES
# 1. only C option is running - solved
# 2. catch out of range errors - solved
# 3. save marked item in the list - solved
# 4. how to unmark item and save in the list - challenge
