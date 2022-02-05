import sqlite3


try:
    sqlite_connection = sqlite3.connect('sqlite_pyth5.db')
    cursor = sqlite_connection.cursor()
    print('База данных успешно созданна и подключена.')
    
    sqlite_select_version_query = 'SELECT sqlite_version();'
    cursor.execute(sqlite_select_version_query)
    record = cursor.fetchall()
    print('Версия SQLite:',record[0][0])
    cursor.close()
except sqlite3.Error as error:
    print('Ошибка при подключении к SQLite:', error)


finally:
    if sqlite_connection:
        sqlite_connection.close()
        print('Соединение с SQLite закрыто.')    



def createTable():
    try:
        sqlite_connection = sqlite3.connect('sqlite_pyth5.db')
        cursor = sqlite_connection.cursor()
        print('База данных успешно созданна и подключена.')

        create_table = '''CREATE TABLE studetns (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            surname TEXT NOT NULL);'''
        cursor.execute(create_table)
        sqlite_connection.commit()
        print('Таблица созданна')

        cursor.close()
    except sqlite3.Error as error:
        print('Ошибка при подключении к SQLite:', error)


    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Соединение с SQLite закрыто.')

def script(name_file):
    try:
        sqlite_connection = sqlite3.connect('sqlite_pyth5.db')
        cursor = sqlite_connection.cursor()
        print('База данных успешно созданна и подключена.')
        try:
            with open(name_file,'r') as file:
                sql_script = file.read()
        except Exception as error:
                    if sqlite_connection:
                        sqlite_connection.close()
                        print('Соединение с SQLite закрыто.')
                    exit(error)
        cursor.executescript(sql_script)    
        sqlite_connection.commit()
        print('Скрипт выполнен успешно.')
        cursor.close()
    except sqlite3.Error as error:
        print('Ошибка при подключении к SQLite:', error)


    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print('Соединение с SQLite закрыто.')

#createTable()
script('create_tables.sql')                