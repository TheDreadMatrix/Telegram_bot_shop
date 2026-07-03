import asyncio

from settings import TELEGRAM_BOT_TOKEN
from databases.db import init_db, close_db

from aiogram import Dispatcher, Bot, Router
from aiogram.types import ErrorEvent

from handlers.starter import starter_router


error_router = Router(name="error")

@error_router.error()
async def error_handler(event: ErrorEvent):
    if event.update.message:
        await event.update.message.answer("❌ Произошла внутренняя ошибка. Попробуйте позже.")
    print(event.exception)

        

dp = Dispatcher()
dp.include_router(starter_router)
dp.include_router(error_router)

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