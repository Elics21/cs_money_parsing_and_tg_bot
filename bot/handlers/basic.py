from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

from bot.keyboard.basicKeyboard import start_keyboard

router = Router()

@router.message(Command(["start", "run"]))
async def start(message: Message):
    await message.answer(text="Выберите категорию", reply_markup=start_keyboard)