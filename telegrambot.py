import asyncio
from aiogram import Bot, Dispatcher, F
from sqlite3 import connect
from pathlib import Path
from app.handlers import router

async def main():
    bot = Bot(token="YOUR TOKEN")
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("off")
