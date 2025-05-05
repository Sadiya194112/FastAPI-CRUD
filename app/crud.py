from app import models
from fastapi import HTTPException
from sqlalchemy.orm import Session


def create_user(db: Session, user):
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    existing_email = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = models.User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    return db_user

def create_task(db: Session, task):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    return db_task


def get_tasks(db: Session):
    return db.query(models.Task).all()


def update_task(db: Session, task_id, updated_task):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    for key, value in updated_task.dict().items():
        setattr(task, key, value)
    db.commit()
    return task


def delete_task(db: Session, task_id):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"detail": "Task deleted"}



