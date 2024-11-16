# from sqlalchemy.ext.asyncio import AsyncEngine
# from sqlmodel import create_engine
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, text
from sqlmodel.ext.asyncio.session import AsyncSession

from src.config import Config

# engine = create_engine(url=Config.DATABASE_URL, echo=True)
# engine = AsyncEngine(create_engine(url=Config.DATABASE_URL, echo=True))
engine = create_async_engine(Config.DATABASE_URL, echo=True)


async def init_db():
    async with engine.begin() as conn:
        from src.books.models import Book

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    Session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

    async with Session() as session:
        yield session
