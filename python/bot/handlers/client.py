
from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from keyboards import kb_main,kb_orders,kb_cancel,kb_login
from keyboards import inline_order_pizza_kb,inline_order_burger_kb,inline_order_roll_kb
from create_bot import bot
from datebase import burgers,pizzas,rolls,login,menu
from handlers import other as oth
from aiogram.dispatcher import FSMContext

global user_data
user_data = []




async def start(message: types.Message):
    await message.reply('Вас приветствует бот тестовой службы доставки! Пожалуйста войдите или зарегистрируйтесь: ',reply_markup=kb_login)



async def cancel_login(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.reply('OK',reply_markup=kb_main)
        return
    await state.finish()
    await message.reply("OK", reply_markup=kb_login)








async def start_login(message: types.Message):
    await oth.login.username.set()
    await message.reply('Введите новый логин',reply_markup=kb_cancel)

async def login_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await oth.login.next()
    await message.reply('Введите пароль')

async def login_userpass(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['pass'] = message.text
        login.addNewUser([data['name'],data['pass']],'delivery.db')
    await message.reply('Пользователь успешно зарегестрирован',reply_markup=kb_login)
    await state.finish()


async def sigin_start(message: types.Message):
    await oth.sigin.username.set()
    await message.reply('Введите имя пользователя',reply_markup=kb_cancel)

async def sigin_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await oth.sigin.next()
    await message.reply('Введите пароль')

async def sigin_userpass(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['userpass'] = message.text
        print(login.CheckUserInfo(data['username'], data['userpass'], 'delivery.db'))
        if login.CheckUserInfo(data['username'],data['userpass'],'delivery.db') == [(data['username'], data['userpass'])]:

            await message.reply('Данные ведены верно',reply_markup=kb_main)
            await state.finish()
            log_data = login.CheckUserInfo(data['username'],data['userpass'],'delivery.db')
            for i in log_data:
                for j in i:
                    user_data.append(j)
        else:
            await message.reply('Данные введены не верно',reply_markup=kb_login)
            await state.finish()

async def caffee_menu(message: types.Message):
    products = menu.SelectTable('delivery.db')
    print(products)
    for prod in products:
        answer = f'''Название: {prod[0]},
Цена товара: {prod[3]},
Ингридиенты: {prod[4]}'''
        await bot.send_photo(message.from_user.id,prod[1],caption=answer)
        type = prod[2]
        if type == 'sushi':
            await bot.send_photo(message.from_user.id, prod[1], caption=answer,reply_markup=inline_order_roll_kb)
            continue
        elif type == 'burger':
            await bot.send_photo(message.from_user.id, prod[1], caption=answer,reply_markup=inline_order_burger_kb)
            continue
        else:
            await bot.send_photo(message.from_user.id, prod[1], caption=answer,reply_markup=inline_order_pizza_kb)
            continue








async def my_orders(message: types.Message):
    await message.reply('OK',reply_markup=kb_orders)

async def my_ordered_rolls(message: types.Message):
    orders = rolls.selectFromUsernames(user_data[0],'delivery.db')
    for order in orders:
        answer = f'''ID заказа: {order[0]},
Имя пользователя: {order[2]},
Адресс доставки: {order[4]},
Наименование товара: {order[5]},
Цена товара: {order[6]},
Ингридиенты: {order[7]}'''
        await bot.send_photo(message.from_user.id,order[1],caption=answer)

async def my_ordered_burgers(message: types.Message):
    orders = burgers.selectFromUsernames(user_data[0],'delivery.db')
    for order in orders:
        answer = f'''ID заказа: {order[0]},
Имя пользователя: {order[2]},
Адресс доставки: {order[4]},
Наименование товара: {order[5]},
Цена товара: {order[6]},
Ингридиенты: {order[7]}'''
        await bot.send_photo(message.from_user.id,order[1],caption=answer)

async def my_ordered_pizzas(message: types.Message):
    orders = pizzas.selectFromUsernames(user_data[0],'delivery.db')
    for order in orders:
        answer = f'''ID заказа: {order[0]},
Имя пользователя: {order[2]},
Адресс доставки: {order[4]},
Наименование товара: {order[5]},
Цена товара: {order[6]},
Ингридиенты: {order[7]}'''
        await bot.send_photo(message.from_user.id,order[1],caption=answer)

async def orders_sum(message: types.Message):
    counter = 0
    pizza = pizzas.selectFromUsernames(user_data[0],'delivery.db')
    burger = burgers.selectFromUsernames(user_data[0],'delivery.db')
    roll = rolls.selectFromUsernames(user_data[0],'delivery.db')
    for item in pizza:
        if item[6] > 0:
            counter += int(item[5])
    for item in burger:
        if item[6] > 0:
            counter += int(item[5])
    for item in roll:
        if item[6] > 0:
            counter += int(item[5])
    await message.reply(f'Цена товаров: {counter}',reply_markup=kb_main)









def register_message_handlers(dp: Dispatcher):
    dp.register_message_handler(start,commands=['start'])
    dp.register_message_handler(cancel_login,Text(equals='Назад',ignore_case=True),state='*')
    dp.register_message_handler(start_login,Text(equals=['Регистрация'],ignore_case=True),state=None)
    dp.register_message_handler(login_username,state=oth.login.username)
    dp.register_message_handler(login_userpass,state=oth.login.userpass)
    dp.register_message_handler(sigin_start,Text(equals=['Вход'],ignore_case=True),state=None)
    dp.register_message_handler(sigin_username,state=oth.sigin.username)
    dp.register_message_handler(sigin_userpass,state=oth.sigin.userpass)
    dp.register_message_handler(caffee_menu,Text(equals=['📜Меню📜']))
    dp.register_message_handler(my_orders,Text(equals='Мои заказы',ignore_case=True),state=None)
    dp.register_message_handler(my_ordered_rolls,Text(equals='🍣Мои Суши🍣',ignore_case=True),state=None)
    dp.register_message_handler(my_ordered_burgers,Text(equals='🍔Мои Бургеры🍔',ignore_case=True),state=None)
    dp.register_message_handler(my_ordered_pizzas,Text(equals='🍕Мои Пиццы🍕',ignore_case=True),state=None)
    dp.register_message_handler(orders_sum,Text(equals='Сумма всех товаров',ignore_case=True),state=None)





