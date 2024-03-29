import json
from aiogram import F, Router
from aiogram.types import Message
from api.get_requests import collect_data

JSON_PATH = "api/result.json"
router = Router()

def get_data(type):
    collect_data(type)
    with open(JSON_PATH) as file:
        data = json.load(file)
    return data

CATEGORY_INDEX = {
    "Агенты": 18,
    "Кейсы": 12
}


@router.message(F.text.in_(CATEGORY_INDEX.keys()))
async def get_discount_knives(message: Message):
    await message.answer("Please waiting...")
    data = get_data(CATEGORY_INDEX.get(message.text))
    for index, item in enumerate(data):
        card = (f"Название: <code>{item.get("full_name")}</code>\n"
                f"3d: <a href='{item.get("3d")}'>*Ссылка*</a>\n"
                f"Скидка: <b>{item.get("discount")}</b>%\n"
                f"Цена: <b>{item.get("price")}$</b>")
        if index%20 == 0:
            pass
        await message.answer(card, disable_web_page_preview=True)