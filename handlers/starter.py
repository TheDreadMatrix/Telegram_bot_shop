from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message


starter_router = Router(name="starter")



@starter_router.message(Command(commands=["start"]))
async def start_handler(message: Message):
    await message.answer("Hello! I am your bot. Use /help to see available commands.")