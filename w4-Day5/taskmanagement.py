# Build a task management system that saves data to files and uses external libraries
import json
import os

path = "file/server.json"

while True:

    choice = input(
        "Task Management System: \n Enter Your choice: \n 1. Add Task 2. View Task 3. Search Task 4. Remove Task 5. Exit :"
    )

    if choice == "Add Task".lower():
        title = input("Enter title for task:")
        desc = input("Enter Description for task")

        with open(path, "r") as r:
            tasks = json.load(r)

        tasks.append({"task": title, "description": desc})

        with open(path, "w") as w:
            json.dump(tasks, w)
            print("Task Added")

    elif choice == "View Task".lower():
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, "r") as r:
                data = json.load(r)

                print("Task:", data["task"])
                print("Description:", data["description"])
        else:
            print("No task found")

    elif choice == "Search Task".lower():
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, "r") as s:
                data = json.load(s)

                search = input("Enter a task title to find: ")
                found = False

                for task in data:
                    if task["task"].lower() == search.lower():
                        print("Task:", task["task"])
                        print("Description:", task["description"])
                        found = True
                        break

                if not found:
                    print("no match found!")
        else:
            print("No task found!")

    elif choice == "Remove Task".lower():
        if os.path.exists(path) and os.path.getsize(path) > 0:
            with open(path, "r") as s:
                data = json.load(s)
                
            remove = input("Enter Task Title to remove:").strip()

            updated_data = [task for task in data if task["task"].lower() != remove.lower()]
            if len(updated_data)== len(data):
                print("Task no found")
            else:
                with open(path, "w") as s:
                    json.dump(updated_data, s)
                print("Task remove successfully")
        else:
            print("No task found")

    elif choice == "exit".lower():
        break

    else:
        print("Invalid Operator ! Please Try Again")
