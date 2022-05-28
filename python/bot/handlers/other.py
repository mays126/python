from aiogram.dispatcher.filters.state import State, StatesGroup

class login(StatesGroup):
    username = State()
    userpass = State()

class sigin(StatesGroup):
    username = State()
    userpass = State()

class adminsigin(StatesGroup):
    adminname = State()
    adminpass = State()

class roll_order(StatesGroup):
    adress = State()
    name = State()

class burger_order(StatesGroup):
    adress = State()
    name = State()

class pizza_order(StatesGroup):
    adress = State()
    name = State()


class add_good(StatesGroup):
    name = State()
    photo = State()
    type = State()
    price = State()
    ingridients = State()

class delete_burger_user(StatesGroup):
    id = State()

class delete_pizza_user(StatesGroup):
    id = State()

class delete_roll_user(StatesGroup):
    id = State()

class delete_admin_order_burger(StatesGroup):
    id = State()

class delete_admin_order_pizza(StatesGroup):
    id = State()

class delete_admin_order_roll(StatesGroup):
    id = State()

class photo(StatesGroup):
    photo = State()