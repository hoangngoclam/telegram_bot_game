from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InputMessageContent, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
import config
from GameComputer import GameComputer


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

button_bua = KeyboardButton("[ 🤛 Búa]")
button_keo = KeyboardButton("[ ✌️ Kéo]")
button_bao = KeyboardButton("[ ✋ Bao]")
button_exit = KeyboardButton("Thoát game")

menu_game = ReplyKeyboardMarkup(one_time_keyboard=True)
menu_game.add(button_bua, button_keo, button_bao)
menu_game.add(button_exit)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("Bạn chọn Búa, kéo hay là Bao", reply_markup=menu_game)

@dp.message_handler()
async def receiveMessage(message: types.Message):
    player_action = ""
    game_computer = GameComputer()
    if(message.text == "[ 🤛 Búa]"):
        player_action = "rock"
    elif(message.text == "[ ✌️ Kéo]"):
        player_action = "scissors"
    elif(message.text == "[ ✋ Bao]"):
        player_action = "paper"
    elif(message.text == "Thoát game"):
        pass
    else:
        await message.answer("Bạn chọn lại đi")
        pass
    game_computer.play(player_action)
    game_play_message = game_computer.get_game_play_message(player_action)
    await message.answer(game_play_message)
    game_result = game_computer.get_result()
    if(game_result == "win"):
        await message.answer("Bạn Chiến Thắng 🏆")
    elif(game_result == "lose"):
        await message.answer("Bạn Đã Thua 🤦‍♂️")
    else :
        await message.answer("Bạn Hòa Với Máy 🤝")
    await welcome(message)

if __name__ == '__main__':
    executor.start_polling(dp)