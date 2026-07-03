from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from bcrypt import gensalt, checkpw, hashpw

from databases.models import User

from handlers import user
from settings import ROLES

from .utils.messages import send_callback_message, send_message


# Login and register state
class RegisterState(StatesGroup):
    username = State()
    password = State()
    role = State()


class LoginState(StatesGroup):
    username = State()
    password = State()




starter_router = Router(name="starter")




@starter_router.message(Command(commands=["logout"]))
async def logout_handler(message: Message, state: FSMContext):
    user = await User.get_or_none(telegram_id=message.from_user.id)
    if user:
        user.telegram_id = None
        await user.save()
        await state.clear()
        await send_message(message, state, "Вы успешно вышли из системы.")
    else:
        await send_message(message, state, "Вы не вошли в систему.")



@starter_router.message(Command(commands=["start"]))
async def start_handler(message: Message, state: FSMContext):
    
    user = await User.get_or_none(telegram_id=message.from_user.id)

    if not user:
        builder = InlineKeyboardBuilder()
        builder.button(text="Войти", callback_data="login")
        builder.button(text="Регистрация", callback_data="register")

        builder.adjust(1)

        await send_message(message, state, "Добро пожаловать! Пожалуйста, выберите действие:", reply_markup=builder.as_markup())

    else:
        await send_message(message, state, f"Привет, {user.username}! Вы уже вошли в систему.")
    

# Login handlers
@starter_router.callback_query(F.data == "login")
async def login_callback_handler(callback: CallbackQuery, state: FSMContext):
    
    await send_callback_message(callback, state, "Введите ваш логин:")
    
    await state.set_state(LoginState.username)



@starter_router.message(LoginState.username)
async def get_login_username_handler(message: Message, state: FSMContext):
    await state.update_data(username=message.text)
  
    await send_message(message, state, "Введите ваш пароль:")
    
    await state.set_state(LoginState.password)


@starter_router.message(LoginState.password)
async def get_login_password_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    username = data["username"]
    password = message.text

    user = await User.get_or_none(username=username)

    if user and checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
        user.telegram_id = message.from_user.id
        await user.save()
        await send_message(message, state, f"✅ Вы успешно вошли в систему, {user.username}!")
        await state.clear()
    else:
        await send_message(message, state, "❌ Неверный логин или пароль. Попробуйте снова.")



# Register handlers
@starter_router.callback_query(F.data == "register")
async def register_callback_handler(callback: CallbackQuery, state: FSMContext):
    await send_callback_message(callback, state, "Введите ваш логин:")
    await state.set_state(RegisterState.username)


@starter_router.message(RegisterState.username)
async def get_username_handler(message: Message, state: FSMContext):
    existing_user = await User.get_or_none(username=message.text)
    if existing_user:
        await send_message(message, state, "❌ Этот логин уже занят. Пожалуйста, введите другой логин:")
    else:
        await state.update_data(username=message.text)
        await send_message(message, state, "Введите ваш пароль:")
        await state.set_state(RegisterState.password)


@starter_router.message(RegisterState.password)
async def get_password_handler(message: Message, state: FSMContext):

    hashed_password = hashpw(message.text.encode("utf-8"), gensalt()).decode("utf-8")

    await state.update_data(password=hashed_password)

    await send_message(message, state, "Введите роль (user/admin):")
    await state.set_state(RegisterState.role)


@starter_router.message(RegisterState.role)
async def get_role_handler(message: Message, state: FSMContext):
    role = message.text.lower()
    if role in ROLES:
        data = await state.get_data()

        await User.create(telegram_id=message.from_user.id, username=data["username"], password=data["password"], role=role)

        await send_message(message, state, "✅ Регистрация завершена!")
        await state.clear()

    
    else:
        await send_message(message, state, "❌ Неверная роль. Пожалуйста, введите 'user' или 'admin'.")
