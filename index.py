from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InputMessageContent, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
import json
import config
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)
@dp.message_handler()
async def kb_answer(message: types.Message):
    info = bot.get("id")
    print(info)
    if message.text == "Account list":
        await message.answer("This is account List")
    elif message.text == "Add Account":
        await message.answer("This is Add Account")
        a = await message.reply("Enter the ID: ", reply_markup=InlineKeyboardMarkup())
    elif message.text == "Delete Account":
        await message.answer("This is Delete Account")

if __name__ == '__main__':
  executor.start_polling(dp)