import os
import json

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return {"tasks": []}

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if tasks["tasks"]:
        print("Your To-Do List:")
        for index, task in enumerate(tasks["tasks"], start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")

def add_task(tasks, new_task):
    tasks["tasks"].append(new_task)
    save_tasks(tasks)
    print(f"Task '{new_task}' added successfully!")

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks["tasks"]):
        removed_task = tasks["tasks"].pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display Tasks\n2. Add Task\n3. Remove Task\n4. Quit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            new_task = input("Enter the new task: ")
            add_task(tasks, new_task)
        elif choice == "3":
            task_index = int(input("Enter the task index to remove: "))
            remove_task(tasks, task_index)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
