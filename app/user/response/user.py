from pydantic import BaseModel
from datetime import datetime


class CreateUserResponse(BaseModel):
    id: int
    email: str
    name: str
    password: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "email": "payhere@gmail.com",
                "name": "payhere",
                "password": "payhere1",
                "created_at": "2022-01-13T07:50:54.289Z",
                "updated_at": "2022-01-13T07:50:54.289Z",
            }
        }


class LoginUserResponse(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "access_token": "token",
                "token_type": "bearer",
            }
        }