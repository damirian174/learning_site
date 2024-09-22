from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String
from base import Base

# Создание модели роль


class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

