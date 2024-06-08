import json

def load_todo_list():
    try:
        with open("todo_list.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_todo_list(todo_list):
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file)

def display_todo_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task(todo_list, task):
    todo_list.append(task)
    save_todo_list(todo_list)

def remove_task(todo_list, task_index):
    if 1 <= task_index <= len(todo_list):
        removed_task = todo_list.pop(task_index - 1)
        save_todo_list(todo_list)
        print(f"Task '{removed_task}' removed.")
    else:
        print("Invalid task index.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\n1. Display To-Do List\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_todo_list(todo_list)
        elif choice == "2":
            task = input("Enter task: ")
            add_task(todo_list, task)
        elif choice == "3":
            display_todo_list(todo_list)
            task_index = int(input("Enter the task index to remove: "))
            remove_task(todo_list, task_index)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
