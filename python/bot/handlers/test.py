from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from create_bot import bot
from keyboards import kb_main,kb_orders,kb_cancel,kb_login,inline_order_pizza_kb,inline_order_burger_kb,inline_order_roll_kb,main_user_menu_kb
from datebase import burgers,pizzas,rolls,login,menu
from handlers import other as oth
from aiogram.dispatcher import FSMContext



async def upload(message: types.Message):
    await oth.photo.photo.set()
    await message.reply('Кинь фото')

async def upload_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        print(str(data['photo']))
        await bot.send_photo(message.from_user.id, 'AgACAgIAAxkBAAIHZWKRBMET9zeYAVN-WlsJoT78XK6QAAKfvjEbIgKJSCgXpbttlLGIAQADAgADcwADJAQ')
    await state.finish()
    await message.reply('OK')


def reg_handlers(dp: Dispatcher):
    dp.register_message_handler(upload,Text(equals='Кинь фотку', ignore_case=True),state=None)
    dp.register_message_handler(upload_2,content_types=['photo'],state=oth.photo.photo)



