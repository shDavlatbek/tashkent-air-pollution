from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column

from db.db import Base
from schemas.users import UserRead
from fastapi_users.db import SQLAlchemyBaseUserTable


# class Users(Base):
#     __tablename__ = "users"
#     pydantic_model = UserSchema
    
#     name: Mapped[str]

class User(SQLAlchemyBaseUserTable[int], Base):
    pydantic_model = UserRead
    
    full_name: Mapped[str] = mapped_column(String(length=150), nullable=False)