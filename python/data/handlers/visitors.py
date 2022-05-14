
from aiogram import Dispatcher, types
from datebase import visitors as vs
from datebase import registred_books as reg
from datebase import books as books
from aiogram.dispatcher import FSMContext
from keyboards import kb_main,kb_vis,kb_books,kb_regs,kb_cancel
from handlers import other as oth
from aiogram.dispatcher.filters import Text



########################################################    ВЫВОД ДАННЫХ ИЗ БАЗЫ    ############################################


async def send_table(message: types.Message):
    try:
        visitors = vs.SelectTable()
        answer = ''
        for visitor in visitors:
            answer = answer + str(visitor[0]) +' ' + visitor[1] + ' '+ visitor[2] + '\n'
        print(answer)
        await message.reply(answer[:-2],reply_markup=kb_main)
    except:
        await message.reply('Таблица пуста')    


     


   


#################################################   ОБНОВЛЕНИЕ ДАННЫЗ О ПОСЕТИТЕЛЕ   ###########################


async def update_visitors(message: types.Message):
    await oth.FSMClient_update.update_name.set()
    await message.reply('Введите новое имя',reply_markup=kb_cancel)

async def update_visitors_enter_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await oth.FSMClient_update.next()
    await message.reply('Введите новую фамилию')

async def update_visitors_surname(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await oth.FSMClient_update.next()
    await message.reply('Введите новый адресс')

async def update_visitors_adress(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
    await oth.FSMClient_update.next()
    await message.reply('Введите номер телефона страрой записи')

async def update_visitors_tel(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['tel'] = message.text
    async with state.proxy() as data:
        vs.UpdateRecord(data['name'],data['surname'],data['adress'],data['tel'])
    await message.reply('Запись обновлена',reply_markup=kb_main)       
    await state.finish()











###################################    ДОБАВЛЕНИЕ ПОСЕТИТЕЛЯ    #############################

  
async def add_visitor(message: types.Message):
    await oth.FSMClient_addNewVisitors.add_visitor_tel.set()
    await message.reply('Введите номер телефона',reply_markup=kb_cancel)

async def add_visior_tel(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['tel'] = message.text
    await oth.FSMClient_addNewVisitors.next()
    await message.reply('Введите имя')

async def add_visitor_name(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await oth.FSMClient_addNewVisitors.next()
    await message.reply('Введите фамилию')

async def add_visitor_surname(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    await oth.FSMClient_addNewVisitors.next()
    await message.reply('Введите адресс')

async def add_visitor_adress(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
    async with state.proxy() as data:
        record = (data['tel'],data['name'],data['surname'],data['adress'])
        vs.addNewVisitor([record])
    await state.finish()
    await message.reply('Запись добавленна',reply_markup=kb_main)    
    

  






###############################################   УДАЛЕНИЕ ПОСЕТИТЕЛЯ ИЗ БАЗЫ   ###################



async def delete_visitor(message: types.Message):
    await oth.FSMClient_delete.delet.set()
    await message.reply('Введите id посетителя',reply_markup=kb_cancel)

async def delete_visitors(message:types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.text
    async with state.proxy() as data:
        vs.deleteRecord(data['id'])
    await state.finish()
    await message.reply('Удалено',reply_markup=kb_main)

  
        



##########################################    ПОИСК ПОСЕТИТЕЛЕЙ ПО ФАМИЛИИ   ################################

async def search(message: types.Message):
    await oth.FSMClient_search.search_surname.set()
    await message.reply('Введите фамилию',reply_markup=kb_cancel)

async def search_surname(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['surname'] = message.text
    async with state.proxy() as data:
        visitors = vs.selectFromSurnames(data['surname'])
        answer = ''
        for visitor in visitors:
            answer = answer + str(visitor[0]) +' ' + visitor[1] + ' '+ visitor[2] + '\n'
        await message.reply(answer[:-2],reply_markup=kb_main)       
    await state.finish()  



    ##################################### КОМАНДА ОТМЕНЫ ########################################


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK", reply_markup=kb_main)



def register_message_handler_visitors(dp:Dispatcher):
    dp.register_message_handler(cancel, Text(equals='Отмена', ignore_case=True), state='*')
    dp.register_message_handler(send_table,Text(equals='Вывести список посетителей'))   
    dp.register_message_handler(update_visitors,Text(equals='Обновить данные о посетителе'),state=None)
    dp.register_message_handler(update_visitors_enter_name,state=oth.FSMClient_update.update_name)
    dp.register_message_handler(update_visitors_surname,state=oth.FSMClient_update.update_surname)
    dp.register_message_handler(update_visitors_adress,state=oth.FSMClient_update.update_adress)
    dp.register_message_handler(update_visitors_tel,state=oth.FSMClient_update.update_tel_num)   
    dp.register_message_handler(add_visitor,Text(equals='Добавить посетителя'),state=None)
    dp.register_message_handler(add_visior_tel,state=oth.FSMClient_addNewVisitors.add_visitor_tel)
    dp.register_message_handler(add_visitor_name,state=oth.FSMClient_addNewVisitors.add_visitor_name)
    dp.register_message_handler(add_visitor_surname,state=oth.FSMClient_addNewVisitors.add_visitor_surname)
    dp.register_message_handler(add_visitor_adress,state=oth.FSMClient_addNewVisitors.add_visitor_adress)       
    dp.register_message_handler(delete_visitor,Text(equals='Удаление пользователя' ),state=None)
    dp.register_message_handler(delete_visitors,state=oth.FSMClient_delete.delet)  
    dp.register_message_handler(search,Text(equals='Поиск пользователя по фамилии' ),state=None)
    dp.register_message_handler(search_surname,state=oth.FSMClient_search.search_surname)