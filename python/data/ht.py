from itertools import count
import sqlite3


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

def insert(records):
    print()
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
    print()        

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

def selectFromNames(name):
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

def printAuthorRecords(authorRecords):
    try:
        print()
        for record in authorRecords:
            print('ID:',record[0])
            print('Название:',record[1])
            print('Автор:',record[2])
            print('Кол-во томов:',record[3])
            print()
    except TypeError:
        print("Никаких данных не возвращенно.")

def printCountRecords(countRecords):
    try:
        print()
        for record in countRecords:
            print('ID:',record[0])
            print('Название:',record[1])
            print('Автор:',record[2])
            print('Кол-во томов:',record[3])
            print()
    except TypeError:
        print("Никаких данных не возвращенно.")

def printNameRecords(nameRecords):
    try:
        print()
        for record in nameRecords:
            print('ID:',record[0])
            print('Название:',record[1])
            print('Автор:',record[2])
            print('Кол-во томов:',record[3])
            print()
    except TypeError:
        print("Никаких данных не возвращенно.")

authorInput = input("Введите автора книги: ")
countInput = int(input('Введите кол-во томов в книге: '))
nameInput = input('Введите название книги: ')

books = recordAuthor(authorInput)
booksAndCounts = recordCount(countInput)
booksAndNames = selectFromNames(nameInput)

print('Выборки: ')
print()
print('По автору: ')
printAuthorRecords(books)   
print('По количеству томов: ')    
printCountRecords(booksAndCounts)
print('Вывод по названию: ')
printNameRecords(booksAndNames)