from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


button_1 = KeyboardButton("/get_anime")
button_2 = KeyboardButton("/Как_тебя_зовут")
button_3 = KeyboardButton("/start")

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button_3).add(button_1).insert(button_2)