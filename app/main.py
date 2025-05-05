from .database import engine
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from .auth.jwt_bearer import jwtBearer
from app.auth.jwt_handler import signJWT
from app import models, schemas, dependencies, crud

models.Base.metadata.create_all(bind=engine)


app = FastAPI()


def check_user(db: Session, data: schemas.UserLogin):
    user = db.query(models.User).filter(models.User.email == data.email, models.User.password == data.password).first()
    if not user:
        return False
    return True

@app.post("/users/")
def register(user: schemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    crud.create_user(db, user)
    return signJWT(user.email)


@app.post("/login/")
def login(user: schemas.UserLogin, db: Session = Depends(dependencies.get_db)):
    if check_user(db, user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid login details!"
        }


@app.post("/tasks/", dependencies=[Depends(jwtBearer())], response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_task(db, task)

@app.get("/tasks/", response_model=list[schemas.TaskWithUser])
def read_tasks(db: Session = Depends(dependencies.get_db)):
    return crud.get_tasks(db)

@app.put("/tasks/{task_id}", dependencies=[Depends(jwtBearer())], response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskCreate, db: Session = Depends(dependencies.get_db)):
    return crud.update_task(db, task_id, task)

@app.delete("/tasks/{task_id}", dependencies=[Depends(jwtBearer())])
def delete_task(task_id: int, db: Session = Depends(dependencies.get_db)):
    return crud.delete_task(db, task_id)


