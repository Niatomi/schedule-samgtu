from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Depends

from database import get_async_session

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy import insert

from schedule.models import Schedule
from schedule.schemas import ScheduleSchema

from auth.base_config import fastapi_users
from auth.models import User

router = APIRouter(
    prefix='/schedule',
    tags=['schedule operations']
)


current_user = fastapi_users.current_user()


@router.post('/add_new_subject', status_code=201)
async def get_specific_operation(schedule_schema: ScheduleSchema,
                                 #  user: User = Depends(current_user),
                                 session: AsyncSession = Depends(
                                     get_async_session)):
    try:
        print(schedule_schema.dict())
        session.add(Schedule(**schedule_schema.dict()))
        await session.commit()
        return 'Schedule saved'
    except Exception as e:
        await session.rollback()
        print('Got exception')
        print(e)


@router.get('/get_all_subjects', status_code=200)
async def add_specific_operation(session: AsyncSession = Depends(get_async_session)):
    query = select(Schedule)
    result = await session.execute(query)
    return [el[0] for el in result.all()]
