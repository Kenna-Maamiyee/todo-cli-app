# main.py

tasks = []

def show_menu():
    print("\n1. Add Task\n2. View Tasks\n3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
      
