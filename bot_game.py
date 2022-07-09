from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InputMessageContent, InlineKeyboardMarkup
from aiogram.dispatcher.filters.state import State, StatesGroup
from Models.GameComputer import GameComputer
from Models.Player import Player
import config
import os

SCORE_PER_GAME = 2
best_score = 0
player = None
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

button_bua = KeyboardButton("[ 🤛 Búa]")
button_keo = KeyboardButton("[ ✌️ Kéo]")
button_bao = KeyboardButton("[ ✋ Bao]")
button_again = KeyboardButton("Chơi lại")
button_exit = KeyboardButton("Thoát game")

menu_game = ReplyKeyboardMarkup(one_time_keyboard=True)
menu_game.add(button_bua, button_keo, button_bao)
menu_game.add(button_again)
menu_game.add(button_exit)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    global player, best_score
    if(message.is_command() or message.text == "Chơi lại"):
        player = Player()
        with open("best_score.txt") as f:
            best_score = int(f.readline())
    await message.answer(
        f"- Điểm cao nhất: {best_score}\n- {player.get_message_score()} \n => Bạn chọn (Búa, kéo hay là Bao)", 
        reply_markup=menu_game
    )

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
    elif(message.text == "Chơi lại"):
        if(player.score > best_score):
            await message.answer(f"😍😍😍 [ New Best Score: {player.score} ] 🥳🥳🥳")
            player.save_score()
        await welcome(message)
    elif(message.text == "Thoát game"):
        if(player.score > best_score):
            await message.answer(f"😍😍😍 [ New Best Score: {player.score} ] 🥳🥳🥳")
            player.save_score()
        return
    else:
        await message.answer("Bạn chọn lại đi")
        return
    game_computer.play(player_action)
    game_play_message = game_computer.get_game_play_message(player_action)
    await message.answer(game_play_message)
    game_result = game_computer.get_result()
    if(game_result == "win"):
        await message.answer("Bạn Chiến Thắng 🏆")
        player.add_score(SCORE_PER_GAME)
    elif(game_result == "lose"):
        await message.answer("Bạn Đã Thua 🤦‍♂️")
        player.minu_score(SCORE_PER_GAME)
    else :
        await message.answer("Bạn Hòa Với Máy 🤝")
    await welcome(message)

if __name__ == '__main__':
    executor.start_polling(dp)