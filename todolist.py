
todolist = ["homework","chores","dinner"]

def checktodo():
    print ("\nTo-do:")
    for x in todolist:
        print(x)
        
def addtodo():
    add = input("What do you want to add?")
    todolist.append(add)
    print("\nTo-do:")
    for x in todolist:
        print(x)
       
def removetodo():
    remove = input("What do you want to remove?")

    todolist.remove(remove)
    print("\nTo-do:")
    for x in todolist:
        print(x)
       
i = 1

while i < 3:
    print ("\nWelcome to my todo list program, you may 'add','remove', 'check', or 'leave' todo") 
    print ("\nMake sure to include all input into the program within quotation marks ")
    command = input ("\nWhat would you like to do?\n")

    if command == "check":

        checktodo()

    elif command == "add":
        addtodo()

    elif command == "remove":
        removetodo()

    elif command == "leave":
        i += 10

    else:
        print ("\nPlease Enter a valid command")
