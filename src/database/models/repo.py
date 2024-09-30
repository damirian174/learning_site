from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker



class LearningRepo:
    def __init__(self, session: AsyncSession, orm_model):
        self.session = session
        self.orm_model = orm_model

    # Получить все записи
    async def get_all(self):
        result = await self.session.execute(select(self.orm_model))
        return result.scalars().all()

    # Получить записи по id
    async def get_one_by_id(self, id: int):
        result = await self.session.execute(select(self.orm_model).where(self.orm_model.id == id))
        return result.scalar_one_or_none()

    # Добавить запись
    async def add_one(self, data):
        new_record = self.orm_model(**data)
        self.session.add(new_record)
        await self.session.commit()
        return new_record

    # Удалить запись
    async def delete_one(self, id: int):
        record = await self.get_one_by_id(id)
        if record:
            await self.session.delete(record)
            await self.session.commit()

    # Изменить запись
    async def change_data_by_id(self, id: int, new_data):
        record = await self.get_one_by_id(id)
        if record:
            for key, value in new_data.items():
                setattr(record, key, value)
            await self.session.commit()
            return record
        return None