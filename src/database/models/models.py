from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import  Column, Integer, String

# Задаем параметры подключения
DATABASE_URL = "postgresql+psycopg2://postgres:postgre@localhost:5432/course_app"

# Создаем подключение к базе данных
engine = create_engine(DATABASE_URL)

# Проверяем подключение
# with engine.connect() as connection:
#     result = connection.execute(text("SELECT version();"))
#     for row in result:
#         print(row)
#создаем базовый класс для моделей
class Base(DeclarativeBase):
    pass


class Role(Base):
    __tablename__ = 'role'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)


