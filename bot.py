import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "8746037896:AAFVd8Egom6XhqIuqIvdhlD_NBBrG1KDBY4"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer("بوتەکەت کار دەکات ✅")

if __name__ == '__main__':
    executor.start_polling(dp)