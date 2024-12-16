from models.database import SessionLocal, init_db
from controllers.task_controller import add_task, list_tasks, complete_task, delete_completed_tasks
from utils.file_manager import export_tasks_to_json

def main_menu():
    init_db()
    db = SessionLocal()

    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Completed Tasks")
        print("5. Export Tasks to JSON")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Task Title: ")
            description = input("Task Description: ")
            add_task(db, title, description)
            print("Task added!")
        elif choice == "2":
            tasks = list_tasks(db)
            for task in tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"[{task.id}] {task.title} - {status} - {task.description}")
        elif choice == "3":
            task_id = int(input("Task ID to mark as completed: "))
            complete_task(db, task_id)
            print("Task marked as completed!")
        elif choice == "4":
            delete_completed_tasks(db)
            print("Completed tasks deleted!")
        elif choice == "5":
            # Exportar tareas directamente a la raíz del proyecto (tasks.json)
            export_tasks_to_json(db)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

    db.close()
