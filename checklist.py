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

# Select function that allows user to CRUD the checklist
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")

# testing all CRUD functions
def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    list_all_items()
    mark_completed(0)

test()

