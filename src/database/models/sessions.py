from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from dotenv import load_dotenv
import os

# Подключение к PostgresSQL через защищеный файл
load_dotenv()
database_url = os.getenv('DATABASE_URL')
# Использование асинхронной библиотеки asyncspg и asyncio
async_engine = create_async_engine(database_url, echo=True)

engine = create_async_engine(database_url)
async_session = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session