from atexit import register
from distutils.log import error
import sqlite3


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

def selectRegistredBooks(visitor: tuple):
    try:
        sqlite_connection = sqlite3.connect("homeTask_sqlite.db")
        cursor = sqlite_connection.cursor()

        select_query = '''SELECT visitor_name, surname,tel_number,adress,book FROM registred_books JOIN visitors 
                          ON visitors.tel_number = registred_books.visitor
                          WHERE visitor = ?'''

        cursor.execute(select_query, (visitor[0],))
        records = cursor.fetchall()
        cursor.close()
        return records
    except sqlite3.Error as error:
        print("При выполнении возникла ошибка:", error)
    finally:
        if sqlite_connection:
            cursor.close()
            sqlite_connection.close()


# records = visitors.SelectTable()
# try:
#     for record in records:
#         vis_books = selectRegistredBooks(record)
#         print(vis_books[0][0], vis_books[0][1], end=': ')
#         for book in vis_books:
#             print(book[4],end=' ')
# except:
#     print('')
