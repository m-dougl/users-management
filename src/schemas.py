from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserSchema(BaseModel):
    username: str 
    birth_date: datetime 
    email: EmailStr