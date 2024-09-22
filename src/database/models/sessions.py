from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from dotenv import load_dotenv
import os

# Подключение к PostgresSQL через защищеный файл
load_dotenv()
database_url = os.getenv('DATABASE_URL')
# Использование асинхронной библиотеки asyncspg и asyncio
async_engine = create_async_engine(database_url, echo=True)
