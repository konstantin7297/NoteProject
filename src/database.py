from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, \
    async_sessionmaker, AsyncEngine
from sqlalchemy.ext.declarative import declarative_base

from configs import DB_NAME, DB_PORT, DB_HOST, DB_PASS, DB_USER

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()

engine: AsyncEngine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """ Функция создает и отдает асинхронную сессию """
    async with async_session_maker() as session:
        yield session
