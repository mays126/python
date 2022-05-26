from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_main_menu = KeyboardButton('Главное меню')
main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_kb.add(button_main_menu)



button_cancel = KeyboardButton('Назад')

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)

button_login = KeyboardButton('Регистрация')
button_signin = KeyboardButton('Вход')
button_admin = KeyboardButton('Admin panel')

kb_login = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_login.add(button_login).add(button_signin).add(button_admin)

button_menu = KeyboardButton('📜Меню📜')
button_orders = KeyboardButton('Мои заказы')


kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(button_orders).row(button_menu)


button_orders_burgers = KeyboardButton('🍔Мои Бургеры🍔')
button_orders_pizzas = KeyboardButton('🍕Мои Пиццы🍕')
button_orders_rolls = KeyboardButton('🍣Мои Суши🍣')
button_orders_sum = KeyboardButton('Сумма всех товаров')

kb_orders = ReplyKeyboardMarkup(resize_keyboard=True)
kb_orders.row(button_orders_pizzas,button_orders_rolls,button_orders_burgers).add(button_cancel,button_orders_sum)


button_admin_add_new_good = KeyboardButton('Добавить товар в меню')
button_admin_select_orders = KeyboardButton('Заказы')


kb_admin_main = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_admin_main.row(button_admin_add_new_good,button_admin_select_orders)

button_admin_delete_order_sushi = KeyboardButton('Суши')
button_admin_delete_order_burger = KeyboardButton('Бургеры')
button_admin_delete_order_pizza = KeyboardButton('Пиццы')

kb_admin_delete_orders = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin_delete_orders.row(button_admin_delete_order_pizza,button_admin_delete_order_sushi,button_admin_delete_order_burger).add(button_main_menu)





