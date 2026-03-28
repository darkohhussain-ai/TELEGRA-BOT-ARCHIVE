import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

API_TOKEN = "8746037896:AAFVd8Egom6XhqIuqIvdhlD_NBBrG1KDBY4"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(msg: types.Message):
    await msg.answer("بوتەکەت کار دەکات ✅")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
