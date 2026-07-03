my_tasks = []
# Store tasks
def add_task():
    task = input("Enter a task: ").strip()
    if task:
        my_tasks.append(task)
        print("Task has been added successfully!")
    else:
        print("Task cannot be empty.")
# display all tasks
def view_tasks():
    if not my_tasks:
        print("Your task list is empty.")
    else:
        print("\nYour Tasks:")
        for number, task in enumerate(my_tasks, start=1):
            print(f"{number}. {task}")
        print()
# Main program
def main():
    while True:
        print(" TO-DO LIST ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            print("Thanks for using the To-Do List!")
            break
        else:
            print("Please enter a valid option.")
main()