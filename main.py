"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types
from transliterate import to_cyrillic, to_latin

API_TOKEN = '5416974893:AAGp0vJnX2qRaQmSeXnd12HT3SkGYZAFXwY'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    res = 'Assalomu alaykum, bu lotin-kiril o\'giruvchi boti'
    res+= '\nIstalgan so\'zni kiriting'
    await message.reply(res)



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    msg = message.text
    if msg.isascii():
        response = to_cyrillic(msg)
        await message.answer(response)
    else:
        response = to_latin(msg)
        await message.answer(response)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)