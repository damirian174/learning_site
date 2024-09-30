from sqlalchemy.ext.asyncio import AsyncSession
#from fastapi import Depends
from src.database.models.models import User, Course, Task, Role, CourseTask
from src.database.models.repo import LearningRepo
from src.database.models.sessions  import get_async_session  # Импортируйте ваш генератор сессий

# Определяем репозитории для каждой модели
user_repo = LearningRepo(session=get_async_session, orm_model=User)
course_repo = LearningRepo(session=get_async_session, orm_model=Course)
task_repo = LearningRepo(session=get_async_session, orm_model=Task)
role_repo = LearningRepo(session=get_async_session, orm_model=Role)
course_task_repo = LearningRepo(session=get_async_session, orm_model=CourseTask)

async def create_user(data: dict):
    async with get_async_session() as session:
        user_repo.session = session
        return await user_repo.add_one(data)

async def get_user_by_id(user_id: int):
    async with get_async_session() as session:
        user_repo.session = session
        return await user_repo.get_one_by_id(user_id)

async def get_all_users():
    async with get_async_session() as session:
        user_repo.session = session
        return await user_repo.get_all()

async def update_user(user_id: int, data: dict):
    async with get_async_session() as session:
        user_repo.session = session
        return await user_repo.change_data_by_id(user_id, data)

async def delete_user(user_id: int):
    async with get_async_session() as session:
        user_repo.session = session
        await user_repo.delete_one(user_id)

# Аналогичные функции можно создать для других моделей (Course, Task, Role, CourseTask)
