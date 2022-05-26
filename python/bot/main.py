from create_bot import dp
from aiogram import executor
import logging
from handlers import client,rolls,admin,burgers,pizza

logging.basicConfig(level=logging.INFO)

client.register_message_handlers(dp)
rolls.register_message_handlers_rolls(dp)
pizza.register_pizza_message_handlers(dp)
burgers.register_message_handlers_burgers(dp)
admin.register_admin_message_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
