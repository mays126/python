
from aiogram import Dispatcher, types
from datebase import visitors as vs
from datebase import registred_books as reg
from datebase import books as books
from aiogram.dispatcher import FSMContext
from keyboards import kb_main,kb_vis,kb_books,kb_regs,kb_cancel
from handlers import other as oth
from aiogram.dispatcher.filters import Text



 



################################################### ВЫВОД КНИГ ###################################


async def send_table_books(message: types.Message):
    try:
        bookos = books.SelectTable()
        answer = ''
        for book in bookos:
            answer = answer + 'ID:' + str(book[0]) +'\n' + book[1] + '\n'+ book[2] + '\n' + str(book[3]) + '\n'+ '\n'
        print(answer)
        await message.reply(answer[:-2],reply_markup=kb_main)
    except:
        await message.reply('Таблица пуста')




##########################################################   ОБНОВЛЕНИЕ ДАННЫХ О КНИГЕ   #################################




async def update_books(message: types.Message):
    await oth.FSMClient_books_update.update_books_name.set()
    await message.reply('Введите название новой книги',reply_markup=kb_cancel)

async def update_books_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await oth.FSMClient_books_update.next()
    await message.reply('Введите автора новой книги')

async def update_books_author(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['author'] = message.text
    await oth.FSMClient_books_update.next()
    await message.reply('Введите количество томов новой книги')

async def update_books_colvotomov(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['colvotomov'] = message.text
    await oth.FSMClient_books_update.next()
    await message.reply('Введите id старой книги')

async def update_book_id(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text
    async with state.proxy() as data:
        books.UpdateRecord(data['name'],data['author'],data['colvotomov'],data['id'])    
    await state.finish()
    await message.reply('Запись обновлена',reply_markup=kb_main)





######################################    ДОБАВЛЕНИЕ КНИГИ     ################################



async def add_book(message: types.Message):
    await oth.FSMClient_addNewBook.add_book_name.set()
    await message.reply('Введите название книги',reply_markup=kb_cancel)

async def add_book_name(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await oth.FSMClient_addNewBook.next()
    await message.reply('Введите автора')

async def add_book_author(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['author'] = message.text
    await oth.FSMClient_addNewBook.next()
    await message.reply('Введите кол-во томов')

async def add_book_toms(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['toms'] = message.text
    async with state.proxy() as data:
        record = (books.maxID()+1,data['name'],data['author'],data['toms'])
        books.addNewBook([record])    
    await state.finish()
    await message.reply('Запись добавлена',reply_markup=kb_main)    



###############################################    УДАЛЕНИЕ КНИГИ ИЗ БАЗЫ   ###################


async def delete_books(message: types.Message):
    await oth.FSMClient_delete_books.books_delete.set()
    await message.reply('Введите фамилию',reply_markup=kb_cancel)

async def delete_books_surname(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    async with state.proxy() as data:
        books.deleteRecord(data['surname'])
    await state.finish()
    await message.reply('Удалено',reply_markup=kb_main)



##################################### КОМАНДА ОТМЕНЫ ########################################


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK", reply_markup=kb_main)



def register_handlers_books(dp: Dispatcher):
    dp.register_message_handler(cancel, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(update_books,Text(equals='Обновить данные о книге'),state=None)
    dp.register_message_handler(update_books_name,state=oth.FSMClient_books_update.update_books_name)
    dp.register_message_handler(update_books_author,state=oth.FSMClient_books_update.update_books_author)
    dp.register_message_handler(update_books_colvotomov,state=oth.FSMClient_books_update.update_books_toms)
    dp.register_message_handler(update_book_id,state=oth.FSMClient_books_update.update_books_id)    
    dp.register_message_handler(send_table_books,Text(equals='Вывести список книг'))
    dp.register_message_handler(add_book,Text(equals='Добавить книгу'),state=None)
    dp.register_message_handler(add_book_name,state=oth.FSMClient_addNewBook.add_book_name)
    dp.register_message_handler(add_book_author,state=oth.FSMClient_addNewBook.add_book_author)
    dp.register_message_handler(add_book_toms,state=oth.FSMClient_addNewBook.add_book_toms)
    dp.register_message_handler(delete_books,Text(equals='Удаление книги' ),state=None)
    dp.register_message_handler(delete_books_surname,state=oth.FSMClient_delete_books.books_delete)
