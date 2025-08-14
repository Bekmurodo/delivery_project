from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    id: Optional[int]
    username:str
    email:str
    password:str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra={
            'example': {
                'username': 'farukh',
                'email': 'farukh.haidar2@gmail.com',
                'password': 'password123',
                'is_staff': False,
                'is_active': True
            }
        }
class Settings(BaseModel):
    authjwt_secret_key: str = '5ffc4280efac0a3b89f3e014d1b3e373eba3bc15b5ea22bc3c6fff60b6de9d89'

class LoginModel(BaseModel):
    username :str
    password:str








