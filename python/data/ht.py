import sqlite3

def VersionCheck():
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('База данных успешно созданна.')

        sqlite_selection_version_query = "SELECT sqlite_version()"
        cursor.execute(sqlite_selection_version_query)
        record = cursor.fetchall()
        print("Версия SQLite:", record[0][0])
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось подключиться к SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")       


def script(name_file):
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

def insert(records):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        insert_query = '''INSERT INTO books (id,book_name,author,colvo_tomov)
                          VALUES (?,?,?,?);'''               
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

def SelectTable():
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM books;"
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

def recordAuthor(author):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM books WHERE author=?;"
        cursor.execute(sqlite_selection_query,(author,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по автору", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def recordCount(count):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM books WHERE colvo_tomov=?;"
        cursor.execute(sqlite_selection_query,(count,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по количеству томов", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

def selectRecords(name):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM books WHERE book_name=?;"
        cursor.execute(sqlite_selection_query,(name,))
        record = cursor.fetchall()
        cursor.close()
        return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по количеству томов", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

a = input("Введите автора книги: ")
b = int(input('Введите кол-во томов в книге: '))
c = input('Введите название книги: ')

books = recordAuthor(a)
booksAndCounts = recordCount(b)
booksAndNames = selectRecords(c)


VersionCheck()
print()
print('Создание таблиц: ')
print()
script('ht_tables.sql')
print()
print('Ввод данных в таблицы: ')
print()
insert(books)
print('Выборки: ')
print()
print('По автору: ')
print()
for book in books:
    print('ID:',book[0])
    print('Название:',book[1])
    print('Автор:',book[2])
    print('Кол-во томов:',book[3])
    print()
print()    
print('По количеству томов: ')
print()    
for book in booksAndCounts:
    print('ID:',book[0])
    print('Название:',book[1])
    print('Автор:',book[2])
    print('Кол-во томов:',book[3])
    print()
print()
print('Вывод по названию: ')
print()
for book in booksAndNames:
    print('ID:',book[0])
    print('Название:',book[1])
    print('Автор:',book[2])
    print('Кол-во томов:',book[3])
    print()