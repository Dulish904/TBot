"""Телеграм бібліотеки"""
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
"""Зовнішні бібліотеки"""
import os, gen_anime, time, datetime
"""Внитрішні бібліотеки"""
import comands
from create_bot import dp, bot

comands.register_handlers_comand(dp)

executor.start_polling(dp, skip_updates=True, on_startup=comands.on_startup)
