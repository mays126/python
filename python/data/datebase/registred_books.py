

import sqlite3

from datebase import visitors
# import visitors

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

def selectRegistredBooks(visitor: tuple):
    try:
        sqlite_connection = sqlite3.connect("homeTask_sqlite.db")
        cursor = sqlite_connection.cursor()

        select_query = '''SELECT visitor_name, surname,tel_number,adress,book FROM registred_books JOIN visitors 
                          ON visitors.tel_number = registred_books.visitor
                          WHERE visitor = ?'''
        print(visitor)
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

def deleteRecord(visitor):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_delete_query = "DELETE FROM registred_books WHERE visitor=?;"
        cursor.execute(sqlite_delete_query,(visitor,))
        sqlite_connection.commit()
        print('Запись', visitor, 'успешно удалена')
    except sqlite3.Error as error:
        print("Не удалось удалить данные.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")  

def UpdateRecord(id,book,visitor):
    try:
        sqlite_connection = sqlite3.connect('homeTask_sqlite.db')
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "UPDATE registred_books SET book=?,visitor=? WHERE id=?;"
        cursor.execute(sqlite_selection_query,(book,visitor,id))
        sqlite_connection.commit()
        print('Запись', id, 'успешно обновленна')
    except sqlite3.Error as error:
        print("Не удалось выбрать данные по количеству томов", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
def PrintRegBooks(reg_books):
    regs = reg_books
    arr = [regs[0][0],regs[0][1]]
    try:
        for books in regs:
            arr.append(books[4])
    except:
        print('Что то пошло не так')
    return arr    
    

#addBook(visitors.selectFromNames('Timur'),'книга15')
print(selectRegistredBooks(visitors.selectFromNames('Timur')))


