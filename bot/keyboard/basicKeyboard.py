from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text="Кейсы"), KeyboardButton(text="Агенты")]
    ],
    resize_keyboard=True)