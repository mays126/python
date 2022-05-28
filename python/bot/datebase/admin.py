import sqlite3


def SelectTable(dbpath):
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM admins;"
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

def CheckUserInfo(adminname,adminpass,dbpath):
    empty = ([])
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        sqlite_selection_query = "SELECT * FROM admins WHERE adminname=? AND adminpass=?;"
        cursor.execute(sqlite_selection_query,(adminname,adminpass))
        record = cursor.fetchall()
        cursor.close()
        try:
            if record == empty:
                return 'doesent exists'
            elif len(record[0]) == 2:
                return 'exists'
        except:
            print('Ошибка')
        finally:
            return record
    except sqlite3.Error as error:
        print("Не удалось выбрать данные поситителей.", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def addNewUser(record: list,dbpath):
    print()
    try:
        sqlite_connection = sqlite3.connect(dbpath)
        cursor = sqlite_connection.cursor()
        print('Соединение с базой данных прошло успешно.')

        insert_query = '''INSERT INTO admins (adminname,adminpass)
                          VALUES (?,?);'''
        cursor.executemany(insert_query,(record,))
        print('Запись добавленна')
        sqlite_connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Не удалось записать информацию", error)
        if sqlite3.Error:
            return 'already exists'
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")



addNewUser(['admin','adminPass'],'../delivery.db')

