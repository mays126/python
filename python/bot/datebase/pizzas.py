import sqlite3

def SelectTable(dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM pizzas;"
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

def selectFromUsernames(name,dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM pizzas WHERE username=?;"
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


def maxID(dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT MAX(id) FROM pizzas;"
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



def addNewPizza(record: list,dbpath):
    print()
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        insert_query = '''INSERT INTO pizzas (id,username,userpass,adress,name,price,ingridients)
                          VALUES (?,?,?,?,?,?,?);'''
        cursor.executemany(insert_query,(record,))
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





def deleteRecordAdmin(id,dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_delete_query = "DELETE FROM pizzas WHERE id=? ;"
        cursor.execute(sqlite_delete_query, (id,))
        sqlite_connection.commit()
        print('Запись', id, 'успешно удалена')
    except sqlite3.Error as error:
        print("Не удалось удалить данные.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")
