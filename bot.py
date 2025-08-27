from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.config import settings

bot = Bot(token=settings.telegram_token)
dp = Dispatcher()

# Обробник команди /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("bot started")

async def start_bot():
    await dp.start_polling(bot)
