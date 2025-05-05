from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    owner_id: int

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: str
    password: str

class TaskWithUser(Task):
    owner: User
