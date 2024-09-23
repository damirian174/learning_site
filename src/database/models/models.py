from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from src.database.models.base import Base
# Создание модели роль


class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)


class Course(Base):
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(600), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)


class Task(Base):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    diff: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    solution: Mapped[str] = mapped_column(String(1000), nullable=True)


class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('role.id'))
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('course.id'))
    login: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(50), nullable=False)

    role: Mapped[Role] = relationship("Role", back_populates="users")
    course: Mapped[Course] = relationship("Course", back_populates="users")


class CourseTask(Base):
    __tablename__ = "course_task"
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('course.id'), primary_key=True)
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey('task.id'),  primary_key=True)

    course: Mapped[Course] = relationship("Course", back_populates="coursetasks")
    task: Mapped[Task] = relationship("Task", back_populates="coursetasks")