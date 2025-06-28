from pydantic import BaseModel, validator
from typing import Optional, List


class SignUpModel(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    password: str
    is_staff: Optional[bool]
    is_active: Optional[bool]

    # Validator goes inside the class
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email format')
        return v.lower()  # Convert email to lowercase

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'username': 'farukhjon',
                'email': 'farukh.haidar2@gmail.com',
                'password': 'password123',
                'is_staff': False,
                'is_active': True
            }
        }
class Settings(BaseModel):
    authjwt_secret_key: str = '5ffc4280efac0a3b89f3e014d1b3e373eba3bc15b5ea22bc3c6fff60b6de9d89'


class LoginModel(BaseModel):
    username: str
    password: str


    items: List[dict]  # Now each_item makes sense

    @validator('items', each_item=True)
    def validate_items(cls, v):
        # Validate each dictionary in the list
        if 'key' not in v:
            raise ValueError('Each item must have "key"')
        return v





