from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from sqlalchemy.exc import NoResultFound

class LearningRepo:
    def __init__(self, session: AsyncSession, orm_model):
        self.session = session
        self.orm_model = orm_model

