import json
from sqlalchemy.orm import Session
from models.task import Task
from pathlib import Path

def export_tasks_to_file(db: Session, file_path: str):
    tasks = db.query(Task).all()
    with open(file_path, "w") as file:
        json.dump([{"id": t.id, "title": t.title, "description": t.description, "completed": t.completed} for t in tasks], file)

def import_tasks_from_file(db: Session, file_path: str):
    with open(file_path, "r") as file:
        tasks = json.load(file)
        for task in tasks:
            new_task = Task(
                id=task["id"], 
                title=task["title"], 
                description=task["description"], 
                completed=task["completed"]
            )
            db.merge(new_task)
        db.commit()

def export_tasks_to_json(db: Session, file_name: str = "tasks.json"):
    """
    Exporta todas las tareas de la base de datos a un archivo JSON en la raíz del proyecto.

    Args:
        db (Session): Sesión de la base de datos.
        file_name (str): Nombre del archivo JSON a crear (por defecto 'tasks.json').
    """
    # Obtener la ruta raíz del proyecto
    project_root = Path(__file__).resolve().parent.parent  # Subimos dos niveles desde `utils`
    file_path = project_root / file_name

    # Obtener todas las tareas de la base de datos
    tasks = db.query(Task).all()

    # Convertir las tareas en un formato serializable
    tasks_data = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
        }
        for task in tasks
    ]

    # Escribir las tareas en el archivo JSON
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(tasks_data, file, indent=4, ensure_ascii=False)
        print(f"Tareas exportadas exitosamente a {file_path}")
    except Exception as e:
        print(f"Error al exportar tareas: {e}")
    """
    Exporta todas las tareas de la base de datos a un archivo JSON.

    Args:
        db (Session): Sesión de la base de datos.
        file_path (str): Ruta del archivo JSON donde se guardarán las tareas.
    """
    # Obtener todas las tareas de la base de datos
    tasks = db.query(Task).all()

    # Convertir las tareas en un formato serializable
    tasks_data = [
        {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
        }
        for task in tasks
    ]

    # Escribir las tareas en el archivo JSON
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(tasks_data, file, indent=4, ensure_ascii=False)
        print(f"Tareas exportadas exitosamente a {file_path}")
    except Exception as e:
        print(f"Error al exportar tareas: {e}")