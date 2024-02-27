import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import text
from config import settings
from models import metadata_obj

async_engine = create_async_engine(
    settings.DATABASE_URL_asyncpg,
    echo=True,
)

async def get_123_sync():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 UNION SELECT 4,5,6"))
        print(f"{await res.first()=}")

async def get_123_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 UNION SELECT 4,5,6"))
        print(f"{await res.first()=}")

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata_obj.create_all)

async def main():
    await create_tables()
    await get_123_sync()
    await get_123_async()

if __name__ == "__main__":
    asyncio.run(main())
