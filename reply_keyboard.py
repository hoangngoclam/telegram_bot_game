from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InputMessageContent, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
import config

bot = Bot(token="5498741687:AAHlcsI3Aiat1PoRbdoDIkJvRfLNi4qHG84")
dp = Dispatcher(bot)

list_account_button = KeyboardButton("List Account")
add_account_button = KeyboardButton("Add Account")
delete_account_button = KeyboardButton("Delete Account")

menuKeyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
menuKeyboard.add(list_account_button, add_account_button, delete_account_button)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply("Hello! This is my Bot", reply_markup=menuKeyboard)

@dp.message_handler()
async def kb_answer(message: types.Message):
    print(message)
    if message.text == "List Account":
        await message.answer("✌️")
    elif message.text == "Add Account":
        await message.answer("This is \"Add Account\"")
    elif message.text == "Delete Account":
        await message.answer("This is \"Delete Account\"")


if __name__ == '__main__':
    executor.start_polling(dp)