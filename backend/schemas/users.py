from typing import Optional
from pydantic import Field

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    full_name: str = Field(min_length=1, max_length=150)  # Optional field


class UserCreate(schemas.BaseUserCreate):
    full_name: str = Field(min_length=1, max_length=150)  # Required field


class UserUpdate(schemas.BaseUserUpdate):
    full_name: Optional[str] = None  # Optional field
    

# class UserSchema(BaseModel):
#     id: int
    
#     email: EmailStr
#     hashed_password: str
#     is_active: bool
#     is_superuser: bool
#     is_verified: bool

#     class Config:
#         from_attributes = True

# class UserSchemaAdd(BaseModel):
#     name: str
