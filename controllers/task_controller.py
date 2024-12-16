from sqlalchemy.orm import Session
from models.task import Task

def add_task(db: Session, title: str, description: str = ""):
    new_task = Task(title=title, description=description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def list_tasks(db: Session):
    return db.query(Task).all()

def complete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.completed = True
        db.commit()
    return task

def delete_completed_tasks(db: Session):
    db.query(Task).filter(Task.completed == True).delete()
    db.commit()
