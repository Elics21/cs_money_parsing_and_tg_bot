from aiogram import Router
from bot.handlers.basic import router as basic_router
from bot.handlers.category import router as category_router

MAIN_ROUTER = Router()
MAIN_ROUTER.include_router(basic_router)
MAIN_ROUTER.include_router(category_router)


