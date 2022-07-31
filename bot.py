import logging, googletrans
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5344187878:AAGrPocoXQJG5NXEwkrfgW7sSKCnwpNGa60'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"Botimizga xush kelibsiz, \n\n Ma'lumotlaringiz: \n\n Ism-Familiya: {message.from_user.first_name} {message.from_user.last_name} \n\n Username: @{message.from_user.username}")

URL = "https://docs.aifrom.dev/eng/dev-2.x/_static/logo.png"

@dp.message_handler(commands=['image', 'img'])
async def send_photo(message: types.Message):
    await bot.send_photo(message.chat.id, types.InputFile.from_url(URL))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)