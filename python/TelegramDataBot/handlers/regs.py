
from aiogram import Dispatcher, types
from datebase import visitors as vs
from datebase import registred_books as reg
from datebase import books as books
from aiogram.dispatcher import FSMContext
from keyboards import kb_main,kb_vis,kb_books,kb_regs,kb_cancel
from handlers import other as oth
from aiogram.dispatcher.filters import Text




#############################################        РЕГИСТРАЦИЯ КНИГИ        ####################################################
async def addbook(message: types.Message):
    await oth.FSMClient_add.add_surname.set()
    await message.reply('Введите фамилию',reply_markup=kb_cancel)


async def enter_surname(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await oth.FSMClient_add.next()
    await message.reply('Введите название книги')


async def book_name(message: types.Message,state: FSMContext):

    async with state.proxy() as data:
        data['book_name'] = message.text
    async with state.proxy() as data: 
        visitor = vs.selectFromSurnames(data['surname'])
        book = data['book_name']
        reg.addBook(visitor,book)
    await message.reply('Добавленно',reply_markup=kb_main)    
    await state.finish()



####################################   ВЫВОД ДАННЫХ ИЗ БАЗЫ   #########################

async def send_table_regs(message: types.Message):
    try:
        bookos = reg.SelectTable()
        answer = ''
        for book in bookos:
            answer = answer + 'ID:' + str(book[0]) +'\n' + str(book[1]) + '\n'+ str(book[2]) +  '\n'+ '\n'
        print(answer)
        await message.reply(answer[:-2],reply_markup=kb_main)
    except:
        await message.reply('Таблица пуста') 



    #################################################   ОБНОВЛЕНИЕ ДАННЫЗ О ЗАРЕГИСТРИРОВАННОЙ КНИГИ   ###########################


async def update_regs(message: types.Message):
    await oth.FSMClient_regs_update.update_regs_id.set()
    await message.reply('Введите id',reply_markup=kb_cancel)

async def update_regs_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text
    await oth.FSMClient_regs_update.next()
    await message.reply('Введите имя посетителя')

async def update_regs_name(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await oth.FSMClient_regs_update.next()
    await message.reply('Введите название книги')

async def update_regs_book(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['book'] = message.text
    async with state.proxy() as data:
        reg.UpdateRecord(int(data['id']),data['name'],data['book'])
    await state.finish()
    await message.reply('Обновлено',reply_markup=kb_main)    




    ###############################################    ВЫВОД ЗАРЕГИСТРИРОВАННЫХ КНИГ И ИХ ПОЛЬЗОВАТЕЛЕЙ   ###################


async def regs(message: types.Message):
    await oth.FSMClient_regs.regs.set()
    await message.reply('Введите имя',reply_markup=kb_cancel)

async def print_regs(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    async with state.proxy() as data:
        answer = reg.PrintRegBooks(reg.selectRegistredBooks(vs.selectFromNames(data['name'])))
        await message.reply(', '.join(answer),reply_markup=kb_main)
    await state.finish()        





    ##################################### КОМАНДА ОТМЕНЫ ########################################


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK", reply_markup=kb_main)



######################################## ХЭНДЛЕРЫ ##########################

def register_message_hanlers_regs(dp:Dispatcher):
    dp.register_message_handler(cancel, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(addbook,Text(equals='Добавить регистрацию'),state=None)
    dp.register_message_handler(enter_surname,state=oth.FSMClient_add.add_surname)
    dp.register_message_handler(book_name,state=oth.FSMClient_add.add_book)
    dp.register_message_handler(update_regs,Text(equals='Обновить данные регистрации'),state=None)
    dp.register_message_handler(update_regs_id,state=oth.FSMClient_regs_update.update_regs_id)
    dp.register_message_handler(update_regs_name,state=oth.FSMClient_regs_update.update_regs_visitor)
    dp.register_message_handler(update_regs_book,state=oth.FSMClient_regs_update.update_regs_book)   
    dp.register_message_handler(regs,Text(equals='Поиск регистрации по имени' ),state=None)
    dp.register_message_handler(print_regs,state=oth.FSMClient_regs.regs)    
    dp.register_message_handler(send_table_regs,Text(equals='Вывести список регистраций'))