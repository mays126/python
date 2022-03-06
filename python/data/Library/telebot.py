import logging 
import visitors as vs

from aiogram import Bot,Dispatcher,executor, types

API_TOKEN = '5170762726:AAExkguqiKAyeCSM_Xvjr7_Eg5dWG4TdO5U'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

@dp.message_handler(commands=['table'])
async def send_table(message: types.Message):
    visitors = vs.SelectTable()
    answer = ''
    for visitor in visitors:
        answer = answer + str(visitor[0]) +' ' + visitor[1] + ' '+ visitor[2] + '\n'
    print(answer)
    await message.reply(answer[:-2])
@dp.message_handler()
async def insert_data(message: types.Message):
    parsed_massage = message.text.split(' ')
    tuple(parsed_massage)
    print(parsed_massage)
    vs.addNewVisitor([parsed_massage])
    await message.answer('Добавленно')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)    