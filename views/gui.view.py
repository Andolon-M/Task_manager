import tkinter as tk
from tkinter import messagebox, simpledialog
from models.database import init_db, SessionLocal
from controllers.task_controller import add_task, list_tasks, complete_task, delete_completed_tasks
from utils.file_manager import export_tasks_to_json

def start_gui():
    # Inicializa la base de datos
    init_db()
    db = SessionLocal()

    # Crear la ventana principal
    root = tk.Tk()
    root.title("Task Manager")
    root.geometry("600x400")

    # Lista para mostrar las tareas
    task_listbox = tk.Listbox(root, width=80, height=20)
    task_listbox.pack(pady=10)

    # Función para cargar las tareas en la interfaz
    def load_tasks():
        task_listbox.delete(0, tk.END)  # Limpia la lista
        tasks = list_tasks(db)
        for task in tasks:
            status = "✔️" if task.completed else "❌"
            task_listbox.insert(tk.END, f"[{task.id}] {status} {task.title} - {task.description}")

    # Función para agregar una tarea
    def handle_add_task():
        title = simpledialog.askstring("Add Task", "Enter the task title:")
        if title:
            description = simpledialog.askstring("Add Task", "Enter the task description:")
            if description:
                add_task(db, title, description)
                messagebox.showinfo("Success", "Task added successfully!")
                load_tasks()

    # Función para marcar una tarea como completada
    def handle_complete_task():
        selected = task_listbox.curselection()
        if selected:
            task_text = task_listbox.get(selected[0])
            task_id = int(task_text.split("]")[0][1:])  # Extraer el ID de la tarea
            complete_task(db, task_id)
            messagebox.showinfo("Success", "Task marked as completed!")
            load_tasks()

    # Función para eliminar tareas completadas
    def handle_delete_completed():
        delete_completed_tasks(db)
        messagebox.showinfo("Success", "Completed tasks deleted!")
        load_tasks()

    # Función para exportar tareas
    def handle_export_tasks():
        export_tasks_to_json(db)
        messagebox.showinfo("Success", "Tasks exported to tasks.json!")

    # Botones
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    btn_add = tk.Button(button_frame, text="Add Task", command=handle_add_task)
    btn_add.grid(row=0, column=0, padx=5)

    btn_complete = tk.Button(button_frame, text="Complete Task", command=handle_complete_task)
    btn_complete.grid(row=0, column=1, padx=5)

    btn_delete = tk.Button(button_frame, text="Delete Completed", command=handle_delete_completed)
    btn_delete.grid(row=0, column=2, padx=5)

    btn_export = tk.Button(button_frame, text="Export to JSON", command=handle_export_tasks)
    btn_export.grid(row=0, column=3, padx=5)

    btn_exit = tk.Button(button_frame, text="Exit", command=root.quit)
    btn_exit.grid(row=0, column=4, padx=5)

    # Cargar tareas iniciales
    load_tasks()

    # Iniciar el bucle principal de Tkinter
    root.mainloop()
