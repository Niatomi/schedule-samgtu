from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from sqlalchemy import Boolean
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import TIMESTAMP
from sqlalchemy import JSON

from fastapi_users.db import SQLAlchemyBaseUserTable

from datetime import datetime


Base = declarative_base()


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )

    username: Mapped[str] = mapped_column(
        "username", String, nullable=False
    )

    registration_date: Mapped[datetime] = mapped_column(
        "registration_date", TIMESTAMP, default=datetime.utcnow()
    )

    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )

    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
    )

    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )