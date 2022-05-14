from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMClient_add(StatesGroup):
    add_surname = State()
    add_book = State()


class FSMClient_update(StatesGroup):
    update_name = State()
    update_surname = State()
    update_adress = State()
    update_tel_num = State()     


class FSMClient_regs_update(StatesGroup):
    update_regs_id = State()
    update_regs_visitor = State()
    update_regs_book = State() 

class FSMClient_books_update(StatesGroup):
    update_books_name = State()
    update_books_author = State()
    update_books_toms = State()
    update_books_id = State()

class FSMClient_addNewVisitors(StatesGroup):
    add_visitor_tel = State()
    add_visitor_name = State()
    add_visitor_surname = State()
    add_visitor_adress = State()

class FSMClient_addNewBook(StatesGroup):
    add_book_name = State()
    add_book_author = State()
    add_book_toms = State()

class FSMClient_regs(StatesGroup):
    regs = State()

class FSMClient_delete(StatesGroup):
    delet = State()

class FSMClient_delete_books(StatesGroup):
    books_delete = State()

class FSMClient_search(StatesGroup):
    search_surname = State()    
