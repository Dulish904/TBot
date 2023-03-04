from aiogram import types, Dispatcher
from create_bot import dp, bot
import datetime
import gen_anime
from keyboard import kb_client

"""=========================Start========================="""
async def on_startup(_):
    print(f"I am Ilive {datetime.datetime.now()}")

"""=========================Client========================="""
# @dp.message_handler(commands=['start', 'help'])
async def command_start(message:types.Message):
    try:
        await message.answer(message.from_user.first_name + ' пошол со мной в личку')
        await bot.send_message(message.from_user.id, message.from_user, reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Напише мне в ЛС чтобы я мог тебе писать\nhttps://t.me/Dulish_one_bot')


# @dp.message_handler(commands='Как_тебя_зовут')
async def name_bot(message:types.Message):
    await message.answer("Mein Name steht unter Waffel")


# @dp.message_handler(commands='get_anime')
async def get_anime_art(message:types.Message):
    await message.answer(gen_anime.img_gen())

"""=========================Admin========================="""

"""=========================General========================="""
# @dp.message_handler()
async def echo_send(message:types.Message):
    if message.text == "Привет" or message.text == "привет":
        await message.answer("Дарова далбаеб")
    if message.text == "300":
        await message.answer("Отсоси у трахториста!")
    if message.text == "@Dulish" or message.text.lower() == "dulish" or message.text.lower() == "Дулиш" or message.text.lower() == "дулиш":
        await message.answer("Не трогай его ато ноги тебе сломаю")


def register_handlers_comand(dp:Dispatcher):
    dp.register_message_handler(command_start, commands='start')
    dp.register_message_handler(name_bot, commands='Как_тебя_зовут')
    dp.register_message_handler(get_anime_art, commands='get_anime')
    dp.register_message_handler(echo_send)
