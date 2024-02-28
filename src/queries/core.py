import asyncio
from sqlalchemy import text
from models import metadata_obj
from database import async_engine, sync_engine

def get_123_sync():
    with sync_engine.connect() as conn:
        res = conn.execute(text("SELECT 1,2,3 UNION SELECT 4,5,6"))
        print(f"{res.first()=}")

async def get_123_async():
    async with async_engine.connect() as conn:
        res = await conn.execute(text("SELECT 1,2,3 UNION SELECT 4,5,6"))
        row = await res.fetchone()
        print(f"{row=}")

async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(metadata_obj.create_all)

def drop_tables():
    with sync_engine.connect() as conn:
        metadata_obj.drop_all(conn)

async def main():
    await create_tables()
    await get_123_async()
    get_123_sync()
    drop_tables()

# Проверяем, что код запускается только если файл запущен как скрипт, а не импортирован в другой файл.
if __name__ == "__main__":
    asyncio.run(main())
