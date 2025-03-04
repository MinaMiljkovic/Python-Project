from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
