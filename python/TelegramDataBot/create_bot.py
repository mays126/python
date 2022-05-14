import imp
from aiogram import Bot,Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN = '5307563561:AAGzCDeVrtMBhq4ALibxftGr1lIg7-vfSek'

storage = MemoryStorage()


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=storage)