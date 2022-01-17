from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    email: str
    name: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "payhere@gmail.com",
                "name": "payhere",
                "password": "payhere1",
            }
        }


class LoginUserRequest(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "payhere@gmail.com",
                "password": "payhere1",
            }
        }