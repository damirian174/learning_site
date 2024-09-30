from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from src.database.models.base import Base

class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    # Определяем отношение к пользователям
    users = relationship("User", back_populates="role")

class Course(Base):
    __tablename__ = "course"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(600), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)

    user = relationship("User", back_populates="courses")
    coursetasks = relationship("CourseTask", back_populates="course")
    tasks = relationship("Task", back_populates="course")

class Task(Base):
    __tablename__ = "task"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('course.id'))  # Добавлено для указания внешнего ключа
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    diff: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    solution: Mapped[str] = mapped_column(String(1000), nullable=True)

    # Определение отношения к курсу

    course = relationship("Course", back_populates="tasks")
    coursetasks = relationship("CourseTask", back_populates="task")  # Добавлено для обратного отношения

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey('role.id'))
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('course.id'))
    login: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(50), nullable=False)

    role = relationship("Role", back_populates="users")
    courses = relationship("Course", back_populates="user")

class CourseTask(Base):
    __tablename__ = "course_task"
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('course.id'), primary_key=True)
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey('task.id'), primary_key=True)

    # Отношение к курсу
    course = relationship("Course", back_populates="coursetasks")
    task: Mapped[Task] = relationship("Task", back_populates="coursetasks")
