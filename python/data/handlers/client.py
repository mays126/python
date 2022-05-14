
from aiogram import Dispatcher, types
from datebase import visitors as vs
from datebase import registred_books as reg
from datebase import books as books
from aiogram.dispatcher import FSMContext
from keyboards import kb_main,kb_vis,kb_books,kb_regs,kb_cancel
from handlers import other as oth
from aiogram.dispatcher.filters import Text




     
async def send_welcome(message: types.Message):
    await message.reply('''Вас приветствует бот для работы с базой данных, пожалуйтса выберите действие:''',reply_markup=kb_main)

#############################################      ТРИГЕРЫ КНОПОК         ######################################

async def visitors(message:types.Message):
    await message.reply('OK',reply_markup=kb_vis)  

async def book(message: types.Message):
    await message.reply('ОК',reply_markup=kb_books)

async def regis(message: types.Message):
    await message.reply('OK',reply_markup=kb_regs)

async def back(message: types.Message):
    await message.reply('ОК',reply_markup=kb_main)


 
    



##################################### КОМАНДА ОТМЕНЫ ########################################


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK", reply_markup=kb_main)       



#################################### ХЭНДЛЕРЫ #####################################################


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(back,Text(equals='Меню', ignore_case=True))
    dp.register_message_handler(visitors,Text(equals='Посетители', ignore_case=True))
    dp.register_message_handler(book,Text(equals='Книги', ignore_case=True))
    dp.register_message_handler(regis,Text(equals='Регистрации', ignore_case=True))
    dp.register_message_handler(cancel, Text(equals='Отмена', ignore_case=True), state='*')   




