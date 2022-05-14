
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_start = KeyboardButton('Меню')

button_cancel = KeyboardButton('Отмена')

button_visitors = KeyboardButton('Посетители')
button_books = KeyboardButton('Книги')
button_regs = KeyboardButton('Регистрации')


button_visitors_print_table = KeyboardButton('Вывести список посетителей')
button_visitors_update = KeyboardButton('Обновить данные о посетителе')
button_visitors_add_visitor = KeyboardButton('Добавить посетителя')
button_visitors_delete_visitor = KeyboardButton('Удаление пользователя')
button_visitors_search = KeyboardButton('Поиск пользователя по фамилии')


button_books_print_table = KeyboardButton('Вывести список книг')
button_books_update = KeyboardButton('Обновить данные о книге')
button_books_add_book = KeyboardButton('Добавить книгу')
button_books_delete = KeyboardButton('Удаление книги')


button_regs_print_table = KeyboardButton('Вывести список регистраций')
button_regs_update_regs = KeyboardButton('Обновить данные регистрации')
button_regs_visitor_registr = KeyboardButton('Поиск регистрации по имени')
button_regs_add_reg  = KeyboardButton('Добавить регистрацию')







kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.row(button_visitors,button_regs,button_books)


kb_vis = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_vis.row(button_visitors_print_table,button_visitors_update,button_visitors_add_visitor).row(button_visitors_delete_visitor,button_visitors_search).add(button_start)



kb_books = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_books.row(button_books_print_table,button_books_update,button_books_add_book,button_books_delete).add(button_start)


kb_regs = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_regs.row(button_regs_print_table,button_regs_update_regs).row(button_regs_visitor_registr,button_regs_add_reg).add(button_start)

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_cancel.add(button_cancel)
