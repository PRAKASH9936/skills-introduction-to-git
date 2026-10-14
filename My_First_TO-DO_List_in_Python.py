
tasks = []

def add_task():
    task = input("Enter your task: ").strip()

    if task:
        tasks.append({"name": task, "completed": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("\nYour to-do list is empty!")
        return

    print("\n===== YOUR TO-DO LIST =====")

    for i, task in enumerate(tasks, start=1):
        if task["completed"]:
            status = "Completed"
        else:
            status = "Pending"

        print(f"{i}. {task['name']} [{status}]")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to complete: "))

        if 1 <= number <= len(tasks):
            tasks[number - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        number = int(input("Enter task number to delete: "))

        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted task: {removed['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def show_summary():
    completed = sum(1 for task in tasks if task["completed"])
    pending = len(tasks) - completed

    print("\n===== TASK SUMMARY =====")
    print("Total tasks:", len(tasks))
    print("Completed tasks:", completed)
    print("Pending tasks:", pending)


def main():
    while True:
        print("\n===== PYTHON TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Task Summary")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            show_summary()
        elif choice == "6":
            print("Thank you for using the To-Do List!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
