import logging
from aiogram import executor
from create_bot import dp
from handlers import client
from handlers import books
from handlers import visitors

logging.basicConfig(level=logging.INFO)


client.register_handlers(dp)
books.register_handlers_books(dp)
visitors.register_message_handler_visitors(dp)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
