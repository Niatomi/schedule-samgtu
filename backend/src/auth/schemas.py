from fastapi_users import schemas
from typing import Generic, List, Optional, TypeVar

from pydantic import BaseModel, EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False


class UserCreate(schemas.BaseUserCreate):
    username: str
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False