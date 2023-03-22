from pydantic import BaseModel
from datetime import datetime
from datetime import timezone

class ScheduleSchema(BaseModel):
    name: str
    datetime_start: datetime
    datetime_end: datetime