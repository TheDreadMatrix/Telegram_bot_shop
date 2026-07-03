from aiogram.types import CallbackQuery
from aiogram.types import Message
from aiogram.fsm.context import FSMContext


async def send_message(message: Message, state: FSMContext, text: str, **kwargs):
    data = await state.get_data()

    if "last_bot_message" in data:
        try:
            await message.bot.delete_message(
                chat_id=message.chat.id,
                message_id=data["last_bot_message"]
            )
        except:
            pass

    msg = await message.answer(text, **kwargs)

    await state.update_data(last_bot_message=msg.message_id)

    return msg

async def send_callback_message(callback: CallbackQuery, state: FSMContext, text: str, **kwargs):
    data = await state.get_data()

    if "last_bot_message" in data:
        try:
            await callback.bot.delete_message(
                chat_id=callback.message.chat.id,
                message_id=data["last_bot_message"]
            )
        except:
            pass

    msg = await callback.message.answer(text, **kwargs)

    await state.update_data(last_bot_message=msg.message_id)

    return msg