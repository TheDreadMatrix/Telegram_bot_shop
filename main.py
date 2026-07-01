import asyncio

from settings import TELEGRAM_BOT_TOKEN
from databases.db import init_db, close_db

from aiogram import Dispatcher, Bot

from handlers.starter import starter_router



dp = Dispatcher()
dp.include_router(starter_router)

async def main():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    await init_db()

    try:
        await dp.start_polling(bot)
    finally:
        await close_db()
        await bot.session.close()


if __name__ == "__main__":
    print("RUNNING")
    asyncio.run(main())