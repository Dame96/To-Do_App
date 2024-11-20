#Varibales 

tasks = []
greet = ("Welcome to To-Do App! Please choose one of 3 options!\n")
options = """Enter '1' to Add Tasks\n'2' to View Tasks or\n'3' to Delete Task\n
Or enter "4" to Quit."""

#Defining Functions for the Core Features

def a_task():
    """Adding a new task to the list"""
    new_task = input('Please enter your new task here, ')
    tasks.append(new_task)
    print(f'Here is your updated task list!{tasks}')

def d_task():
    """Removing a task from the list"""
    print(tasks)
    del_task = input('Please enter task would you like to delete, ')
    tasks.remove(del_task)
    print(f'Here is your updated task list!{tasks}')

def v_task():
    """View the current tasks in the list"""
    print(f'Here are your current tasks!{tasks}')

# Program Starting here

print(greet)
print(options)

active = True
while active:
    try:
        choice = int(input("What would you like to do? "))
        if choice not in [1,2,3,4,]:
            print("That option doesn't exist,Please enter a number 1-4")

        if choice == 4:
           active = False
           print('This Program will now end! Have a Great Day!')
           break
        elif choice == 3:
            d_task()
            continue
        elif choice == 2:
            if tasks:
                v_task()
            else: 
                print("Your Task list is currently empty, enter '1' to add a task")
            continue
        elif choice == 1:
            a_task()
            continue

    except ValueError:
        print('Error occurred! Please enter number or correct value!')
    except TypeError:
        print('Error occurred! Please enter an option from the list!')
    except Exception:
        print('Something went wrong! Please select a valid option from the list!')
    
