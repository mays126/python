from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API ='5307563561:AAGzCDeVrtMBhq4ALibxftGr1lIg7-vfSek'

storage = MemoryStorage()

bot = Bot(token=API)
dp = Dispatcher(bot,storage=storage)
