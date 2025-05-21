import json
import os
from datetime import datetime

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, title, description=""):
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def remove_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task {task_id} removed successfully!")
                return
        print(f"Task {task_id} not found!")

    def mark_complete(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"Task {task_id} marked as complete!")
                return
        print(f"Task {task_id} not found!")

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available!")
            return

        print("\nYour Tasks:")
        print("-" * 50)
        for task in self.tasks:
            status = "✓" if task["completed"] else " "
            print(f"[{status}] Task {task['id']}: {task['title']}")
            if task['description']:
                print(f"    Description: {task['description']}")
            print(f"    Created: {task['created_at']}")
            print("-" * 50)

def main():
    todo = TodoApp()
    
    while True:
        print("\nTo-Do App Menu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Complete")
        print("4. View All Tasks")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            todo.add_task(title, description)
        
        elif choice == "2":
            task_id = int(input("Enter task ID to remove: "))
            todo.remove_task(task_id)
        
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as complete: "))
            todo.mark_complete(task_id)
        
        elif choice == "4":
            todo.display_tasks()
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 