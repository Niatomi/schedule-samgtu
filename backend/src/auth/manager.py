from fastapi import Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, Request

from fastapi_users import exceptions, models, schemas
from fastapi_users.db import BaseUserDatabase
from fastapi_users.jwt import SecretType, decode_jwt, generate_jwt
from fastapi_users.password import PasswordHelper, PasswordHelperProtocol
from fastapi_users.types import DependencyCallable
from fastapi_users import BaseUserManager, IntegerIDMixin

from typing import Optional

from auth.models import User
from auth.utils import get_user_db
from config import SECRET

from typing import Optional


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")
        

async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
