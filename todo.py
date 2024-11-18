#Varibales 

tasks = []
greet = ("Welcome to To-Do App! Please choose one of 3 options!")
options = "Enter '1' to Add Task,'2' to View Tasks, or '3' to Delete Task,"
options += ' Or enter "4" to Quit.'

#Defining Fuctionss for the Core Features

def a_task():
    """Adding a new task to the list"""
    tasks.append(new_task)
    print(f'Here is your updated task list!{tasks}')

def d_task():
    """Removing a task from the list"""
    tasks.remove(del_task)
    print(f'Here is your updated task list!{tasks}')

def v_task():
    """View the current tasks in the list"""
    print(f'Here are your current tasks!{tasks}')
    
print(greet)
print(options)

active = True
while active:
    try:
        choice = input("What would you like to do? ")
        if choice == "4":
           active = False
           print('This Program will now end! Have a Great Day!')
           break
        elif choice == "1":
            new_task = input('Please enter your new task here, ')
            a_task()
        elif choice == "2":
            v_task()
        elif choice ==  "3":
            print(tasks)
            del_task = input('What task would you like to delete?')
            d_task()
    except ValueError:
        print('Error occurred! Please enter an option from the list!')
    except TypeError:
        print('Error occurred! Please enter an option from the list!')
    except Exception:
        print('Something went wrong! Please select one of the listed options!')
    finally:
        print(f'Please choose an option or press 4 to end! {options}')

        
    
#To-Do 
# Implement error handling using try, except, else, and finally blocks to catch errors
# Alert the user if they provide invalid input
# Alert the user if there are no tasks to view
# Alert the user if they try to delete a task that doesn't exist
# Alert the user if they select an option on the main menu that doesn't exist
