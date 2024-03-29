from aiogram import Bot, Dispatcher

from config import TOKEN
from bot.handlers.routers import MAIN_ROUTER
import asyncio
import logging

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher()

async def main():
    dp.include_router(MAIN_ROUTER)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
