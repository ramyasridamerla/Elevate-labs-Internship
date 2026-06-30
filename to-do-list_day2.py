# Simple To-Do List Program

to_do_list = []   # Empty list to store tasks

while True:

    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add Task
    if choice == "1":
        task = input("Enter your task: ")
        to_do_list.append(task)   # Add task to list

        # Save task in file
        file = open("ramya.txt", "a")
        file.write(task + "\n")
        file.close()

        print("Task Added!")

    # View Tasks
    elif choice == "2":
        if len(to_do_list) == 0:
            print("No Tasks Available")
        else:
            print("\nYour Tasks:")
            for i in range(len(to_do_list)):
                print(i + 1, ".", to_do_list[i])

    # Remove Task
    elif choice == "3":
        if len(to_do_list) == 0:
            print("No Tasks to Remove")
        else:
            print("\nYour Tasks:")
            for i in range(len(to_do_list)):
                print(i + 1, ".", to_do_list[i])

            n = int(input("Enter task number to remove: "))
            to_do_list.pop(n - 1)   # Remove task
            print("Task Removed!")

    # Exit Program
    elif choice == "4":
        print("Thank You!")
        break

    # Invalid Choice
    else:
        print("Invalid Choice")