from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password : str

class UserResponse(BaseModel):
    # id : int
    username :str
    email :EmailStr
    is_active: bool
    is_superuser: bool

    class Config:
        from_attributes = True