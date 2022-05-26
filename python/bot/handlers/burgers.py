from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from keyboards import kb_main,kb_orders,kb_cancel,kb_login,inline_order_pizza_kb,inline_order_burger_kb,inline_order_roll_kb
from datebase import burgers,pizzas,rolls,login,menu
from handlers import other as oth
from aiogram.dispatcher import FSMContext
from handlers.client import user_data


async def burger_order_start(callback: types.CallbackQuery):
    await oth.burger_order.adress.set()
    await callback.message.reply('Введите адресс доставки')
    await callback.answer('')

async def burger_order_adress(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
    await oth.burger_order.next()
    await message.reply('Введите название выбранного рбургера')

async def burger_order_name(message: types.Message,state: FSMContext):
    menu_data = menu.SelectTable('delivery.db')
    async with state.proxy() as data:
        data['name'] = message.text
        print(data['name'])
        some_data = {}
        try:
            for i in menu_data:
                if i[1] == 'burger' and i[0] == data['name']:
                    some_data['id'] = rolls.maxID('delivery.db') + 1
                    some_data['username'] = user_data[0]
                    some_data['userpass'] = user_data[1]
                    some_data['user_adress'] = data['adress']
                    some_data['name'] = data['name']
                    some_data['price'] = i[2]
                    some_data['ingridients'] = i[3]
            burgers.addNewBurger([some_data['id'],some_data['username'],some_data['userpass'],some_data['user_adress'],some_data['name'],some_data['price'],some_data['ingridients']],'delivery.db')
            await message.reply('Заказ произведён успешно')
        except:
            await message.reply('Бургеров с таким названием не существует',reply_markup=kb_main)
        finally:
            await state.finish()





def register_message_handlers_burgers(dp: Dispatcher):
    dp.register_callback_query_handler(burger_order_start,text='Ordered burger',state=None)
    dp.register_message_handler(burger_order_adress,state=oth.burger_order.adress)
    dp.register_message_handler(burger_order_name,state=oth.burger_order.name)
