from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import TIMESTAMP

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from datetime import datetime

Base = declarative_base()


class Schedule(Base):
    __tablename__ = "schedule_table"
    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    name: Mapped[str] = mapped_column(
        String,
        nullable=False
    )

    datetime_start: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        default=datetime.utcnow()
    )

    datetime_end: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        default=datetime.utcnow()
    )
