from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List
import asyncio
# Предположим, что у тебя есть доступ к ORM-моделям и базовой логике
from models import Task, User
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

class SUser(BaseModel):
    name: str
    email: str

class STask(BaseModel):
    title: str
    description: str

router = APIRouter()

@router.get("/tasks", response_model=List[STask])
async def get_all(session: AsyncSession):
    result = await session.execute(select(Task))
    tasks = result.scalars().all()
    return tasks

@router.get("/users/{id}", response_model=SUser)
async def get_one_by_id(id: int, session: AsyncSession):
    result = await session.execute(select(User).where(User.id == id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/users", response_model=SUser)
async def add_one(data: SUser, session: AsyncSession):
    new_user = User(**data.dict())
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

@router.delete("/users/{id}")
async def delete_one(id: int, background_tasks: BackgroundTasks, session: AsyncSession):
    result = await session.execute(select(User).where(User.id == id))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    background_tasks.add_task(delayed_deletion, user, session)
    return {"message": "Deletion scheduled"}

async def delayed_deletion(user: User, session: AsyncSession):
    await asyncio.sleep(5)  # Задержка 5 секунд перед удалением
    await session.delete(user)
    await session.commit()


@router.patch("/tasks/{id}", response_model=STask)
async def change_data_by_id(id: int, new_data: STask, session: AsyncSession):
    result = await session.execute(select(Task).where(Task.id == id))
    task = result.scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    for key, value in new_data.dict(exclude_unset=True).items():
        setattr(task, key, value)

    await session.commit()
    await session.refresh(task)
    return task



