from fastapi import FastAPI
from fastapi import Depends
import uvicorn
import configparser

from auth.base_config import fastapi_users
from auth.base_config import auth_backend

from auth.schemas import UserCreate
from auth.schemas import UserRead

from auth.models import User
from schedule.router import router as schedule_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Расписание",
    description="API для работы с расписанием",
    version="0.0.1"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    schedule_router,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def main():
    config = configparser.ConfigParser()
    config.read('./config/config.ini')

    is_dev = config.getboolean('dev', 'is_dev')
    port = config.getint('app', 'port')
    host = config.get('app', 'host')

    uvicorn.run("main:app", reload=is_dev, port=port, host=host)


if __name__ == "__main__":
    main()
