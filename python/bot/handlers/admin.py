from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from keyboards import kb_admin_main,kb_admin_delete_orders,kb_login,kb_cancel,main_menu_kb
from keyboards import inline_delete_roll_kb_admin ,inline_delete_burger_kb_admin ,inline_delete_pizza_kb_admin
from datebase import burgers,pizzas,rolls,login,menu,admin
from handlers import other as oth
from aiogram.dispatcher import FSMContext



async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.reply("OK", reply_markup=kb_admin_main)
        return
    await state.finish()
    await message.reply('OK',reply_markup=kb_admin_main)



async def admin_check(message: types.Message):
    await oth.adminsigin.adminname.set()
    await message.reply('Введите имя админа', reply_markup=kb_cancel)


async def admin_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await oth.adminsigin.next()
    await message.reply('Введите пароль')


async def admin_userpass(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['userpass'] = message.text
        print(admin.CheckUserInfo(data['username'], data['userpass'], 'delivery.db'))
        if admin.CheckUserInfo(data['username'], data['userpass'], 'delivery.db') == [(data['username'], data['userpass'])]:

            await message.reply('Данные ведены верно', reply_markup=kb_admin_main)
            await state.finish()
        else:
            await message.reply('Данные введены не верно', reply_markup=kb_login)
            await state.finish()


async def add_good_start(message: types.Message):
    await oth.add_good.name.set()
    await message.reply('Введите название товара',reply_markup=main_menu_kb)

async def add_good_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await oth.add_good.next()
    await message.reply('Введите тип товара')

async def add_good_type(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['type'] = message.text
        if data['type'] == 'pizza' or data['type'] == 'sushi' or data['type'] == 'burger':
            await oth.add_good.next()
            await message.reply('Введите цену')
        else:
            await state.finish()
            await message.reply('Такого типа товара не существует',reply_markup=kb_admin_main)

async def add_good_price(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['price'] = int(message.text)
    await oth.add_good.next()
    await message.reply('Введите ингридиенты')

async def add_good_ingridients(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['ingridients'] = message.text
        menu.addNewProduct([data['name'],data['type'],data['price'],data['ingridients']],'delivery.db')
    await state.finish()
    await message.reply('Успешно добавленно',reply_markup=kb_admin_main)

async def select_orders(message: types.Message):
    await message.reply('OK',reply_markup=kb_admin_delete_orders)

async def select_orders_rolls(message: types.Message):
    items = rolls.SelectTable('delivery.db')
    for item in items:
        answer1 = f'''ID заказа: {item[0]},
Имя пользователя: {item[1]},
Адресс доставки: {item[3]},
Наименование товара: {item[4]},
Цена товара: {item[5]},
Ингридиенты: {item[6]}'''
        await message.reply(answer1,reply_markup=inline_delete_roll_kb_admin)

async def select_orders_pizzas(message: types.Message):
    items = pizzas.SelectTable('delivery.db')
    for item in items:
        answer2 = f'''ID заказа: {item[0]},
Имя пользователя: {item[1]},
Адресс доставки: {item[3]},
Наименование товара: {item[4]},
Цена товара: {item[5]},
Ингридиенты: {item[6]}'''
        await message.reply(answer2,reply_markup=inline_delete_pizza_kb_admin)

async def select_orders_burgers(message: types.Message):
    items = burgers.SelectTable('delivery.db')
    for item in items:
        answer3 = f'''ID заказа: {item[0]},
Имя пользователя: {item[1]},
Адресс доставки: {item[3]},
Наименование товара: {item[4]},
Цена товара: {item[5]},
Ингридиенты: {item[6]}'''
        await message.reply(answer3,reply_markup=inline_delete_burger_kb_admin)




async def delete_order_burger_start(callback: types.CallbackQuery):
    await oth.delete_admin_order_burger.id.set()
    await callback.message.reply('Введите id заказанного бургера')
    await callback.answer('')

async def delete_order_burger(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id'] = message.text
        burgers.deleteRecordAdmin(data['id'],'delivery.db')
        await message.reply('Успешно удаленно')
    except:
        await message.reply('Бургеров с таким id не существует')
    finally:
        await state.finish()


async def delete_order_pizza_start(callback: types.CallbackQuery):
    await oth.delete_admin_order_pizza.id.set()
    await callback.message.reply('Введите id заказанной пиццы')
    await callback.answer('')

async def delete_order_pizza(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id'] = message.text
        pizzas.deleteRecordAdmin(data['id'],'delivery.db')
        await message.reply('Успешно удаленно')
    except:
        await message.reply('Пиццы таким id не существует')
    finally:
        await state.finish()

async def delete_order_roll_start(callback: types.CallbackQuery):
    await oth.delete_admin_order_roll.id.set()
    await callback.message.reply('Введите id заказанных роллов')
    await callback.answer('')

async def delete_order_roll(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['id'] = message.text
        rolls.deleteRecordAdmin(data['id'],'delivery.db')
        await message.reply('Успешно удаленно')
    except:
        await message.reply('Роллов с таким id не существует')
    finally:
        await state.finish()


def register_admin_message_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_check,Text(equals=['Admin panel'],ignore_case=True),state=None)
    dp.register_message_handler(admin_username,state=oth.adminsigin.adminname)
    dp.register_message_handler(admin_userpass,state=oth.adminsigin.adminpass)
    dp.register_message_handler(cancel,Text(equals='Главное меню',ignore_case=True),state='*')
    dp.register_message_handler(add_good_start,Text(equals='Добавить товар в меню', ignore_case=True),state=None)
    dp.register_message_handler(add_good_name,state=oth.add_good.name)
    dp.register_message_handler(add_good_type,state=oth.add_good.type)
    dp.register_message_handler(add_good_price,state=oth.add_good.price)
    dp.register_message_handler(add_good_ingridients,state=oth.add_good.ingridients)
    dp.register_message_handler(select_orders,Text(equals='Заказы',ignore_case=True),state=None)
    dp.register_message_handler(select_orders_rolls,Text(equals='Суши', ignore_case=True),state=None)
    dp.register_message_handler(select_orders_burgers, Text(equals='Бургеры', ignore_case=True), state=None)
    dp.register_message_handler(select_orders_pizzas, Text(equals='Пиццы', ignore_case=True), state=None)
    dp.register_callback_query_handler(delete_order_burger_start,text='delete order burger admin',state=None)
    dp.register_message_handler(delete_order_burger,state=oth.delete_admin_order_burger.id)
    dp.register_callback_query_handler(delete_order_pizza_start,text='delete order pizza admin',state=None)
    dp.register_message_handler(delete_order_pizza,state=oth.delete_admin_order_pizza.id)
    dp.register_callback_query_handler(delete_order_roll_start,text='delete order roll admin',state=None)
    dp.register_message_handler(delete_order_roll,state=oth.delete_admin_order_roll.id)



