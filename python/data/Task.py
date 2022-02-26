from atexit import register
import sqlite3

def maxID():
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT MAX(id) FROM registred_books;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchone()
        cursor.close()
        if record[0] == None:
            return 0
        return record[0]
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def SelectTable():
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM registred_books;"
        cursor.execute(sqlite_selection_query)
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные из таблицы.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def script(name_file):
    print()
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')
        try:
            with open (name_file,'r') as file:
                sql_script = file.read()
        except Exception as error:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print('Соединение с SQLite закрыто.')
                    exit(error)
        cursor.executescript(sql_script)
        sqlite_connection.commit()
        print("Скрипт выполнен успешно")
        cursor.close() 
    except sqlite3.Error as error:
        print("Не удалось выполнить скрипт.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def addNewVisitor(records):
    print()
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        insert_query = '''INSERT INTO visitors (tel_number,visitor_name,surname,adress,registred_book_name)
                          VALUES (?,?,?,?,?);'''               
        cursor.executemany(insert_query,records)
        print('Запись добавленна')
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось записать информацию", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
    print()

def UpdateRecord(name,surname,adress,book_name,tel):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "UPDATE visitors SET visitor_name=?,surname=?,adress=?,registred_book_name=? WHERE tel_number=?;"
        cursor.execute(sqlite_selection_query,(name,surname,adress,book_name,tel))
        sqlite_connection.commit()
        print('Запись', tel, 'успешно обновленна')
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по количеству томов", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def deleteRecord(id):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_delete_query = "DELETE FROM registred_books WHERE id=?;"
        cursor.execute(sqlite_delete_query,(id,))
        sqlite_connection.commit()
        print('Запись', id, 'успешно удалена')
    except sqlite3.Error as error:
        print("Не удалось удалить данные.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def selectFromNames(name):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM visitors WHERE visitor_name=?;"
        cursor.execute(sqlite_selection_query,(name,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по именам поситителей.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def selectFromSurnames(surname):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM visitors WHERE surname=?;"
        cursor.execute(sqlite_selection_query,(surname,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по фамилиям поситителей.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def selectFromAdress(adress):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM visitors WHERE adress=?;"
        cursor.execute(sqlite_selection_query,(adress,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по адрессам поситителей.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def FindFromNumber(tel):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM visitors WHERE tel_number=?;"
        cursor.execute(sqlite_selection_query,(tel,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по именам поситителей.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def printRecords(records):

    try:
        print()
        for record in records:
            print('Телефон:',record[0])
            print('Имя:',record[1])
            print('Фамилия:',record[2])
            print('адресс:',record[3])
            print('Зарег. книга:',record[4])
            print()
    except TypeError:
        print("Никаких данных не возвращенно.")

def selectBooks(book: tuple):
    try:
        sqlite_connection = sqlite3.connect("homeTask_sqlite.db")
        cursor = sqlite_connection.cursor()

        select_query = '''SELECT visitor_name, surname, registred_book_name FROM visitors JOIN books 
                          ON books.book_name = visitors.registred_book_name
                          WHERE registred_book_name = ?'''

        cursor.execute(select_query, (book[1],))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При выполнении возникла ошибка:", error)
    finally:
        if sqlite_connection:
            cursor.close()
            sqlite_connection.close()

def addBook(visitor: tuple,book_name):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()

        insert_query = 'INSERT INTO registred_books (id,book,visitor) VALUES (?,?,?);'
        cursor.execute(insert_query,(maxID()+1,book_name,visitor[0][0]))
        sqlite_connection.commit()
        cursor.close()
        print('Книга',book_name,' зарегестрированна на имя',visitor[0][1],visitor[0][2],'проживающего по адрессу', visitor[0][3])
    except sqlite3.Error as error:
        print('При выполнении возникла ошибка', error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()       

def selectRegistredBooks(visitor: tuple):
    try:
        sqlite_connection = sqlite3.connect("homeTask_sqlite.db")
        cursor = sqlite_connection.cursor()

        select_query = '''SELECT visitor_name, surname,tel_number,adress,book FROM registred_books JOIN visitors 
                          ON visitors.tel_number = registred_books.visitor
                          WHERE visitor = ?'''

        cursor.execute(select_query, (visitor[0][0],))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При выполнении возникла ошибка:", error)
    finally:
        if sqlite_connection:
            cursor.close()
            sqlite_connection.close()

print(selectRegistredBooks(selectFromNames('Olga')))
