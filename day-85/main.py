# Day 85: Simple To-Do List App (Console Version)

def display_tasks(tasks):
    print("\nYour To-Do List:")
    if not tasks:
        print("  No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")

def main():
    tasks = []
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            task = input("Enter the task: ").strip()
            if task:
                tasks.append(task)
                print("Task added.")
            else:
                print("Empty task not added.")
        elif choice == '2':
            display_tasks(tasks)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
