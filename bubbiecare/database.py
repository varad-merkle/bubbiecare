import os
from load_dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker, create_async_engine)

load_dotenv()

engine = create_async_engine(os.getenv("DATABASE_URL"), echo=True)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    async with SessionLocal() as session:
        yield session