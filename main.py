import sqlite3
import pandas as pd

#Соединение с базой данных
connection = sqlite3.connect('my_database.db')
#Курсор нужен для взаимодействия с базой данных
cursor = connection.cursor()


#Подсоединяемся к таблице через имя пользователя и пароль
def admin():
    name = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")
    if name == "Иван" and password == "123":
    #Создание таблицы данных (названия не меняем, иначе все сломается)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Items (
        № INTEGER PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        date DATE NOT NULL
        )
        ''')
        start()
    else:
        print("Введено неправильное имя или пароль")
        connection.close()

def start():
    comand = input("")
    if comand == "ввести данные":
        input_info()
    elif comand == "изменить данные":
        update_info()
    elif comand == "удалить данные":(
        delete_info())
    elif comand == "закрыть":
        #Сохраняем изменения и закрываем соединение
        connection.commit()
        connection.close()
    elif comand == "экспорт в excel":
        give_excel()
    else:
        print("Команда не принята")

#Введение данных(пока через консоль)
def input_info():
    name = input("Введите название товара: ")
    quantity = input("Введите количество товара: ")
    price = input("Введите цену товара: ")
    date = input("Введите дату: ")
    # Добавляем новый предмет
    cursor.execute('INSERT INTO Items (name, quantity, price,  date) VALUES (?, ?, ?, ?)', (name, quantity, price, date))
    connection.commit()
    start()

#Изменение данных(пока через консоль)
def update_info():
    place = input("Какой товар: ")
    ask = input("Изменить: ")
    if ask == "название":
        name_new = input("")
        #Изменение предметов
        cursor.execute('UPDATE Items SET name = ? WHERE name = ?', (name_new, place))
        connection.commit()
        start()
    elif ask == "количество":
        quantity_new = input("")
        cursor.execute('UPDATE Items SET quantity = ? WHERE name = ?', (quantity_new, place))
        connection.commit()
        start()
    elif ask == "цена":
        price_new = input("")
        cursor.execute('UPDATE Items SET price = ? WHERE name = ?', (price_new, place))
        connection.commit()
        start()
    elif ask == "время":
        date_new = input("")
        cursor.execute('UPDATE Items SET date = ? WHERE name = ?', (date_new, place))
        connection.commit()
        start()
    else:
        print("Команда не принята")
        start()

#Удаление данных (пока через консоль)
def delete_info():
    part = input("№ товара: ")
    #удаление объектов
    cursor.execute('DELETE FROM Items WHERE № = ?', (part,))
    connection.commit()
    start()

#Выведение в ексель (пока через консоль)
def give_excel():
    #Выбираем все предметы
    cursor.execute('SELECT * FROM Items')
    items = cursor.fetchall()
    #Создаем список для хранения данных
    data = []
    #Создаем словарь информации
    for item in items:
        data.append({
            '№' : item[0],
            'name': item[1],
            'quantity': item[2],
            'price': item[3],
            'date': item[4]
        })
    #Создаем DataFrame из списка данных
    user_dict = pd.DataFrame(data)
    #Экспорт в файл Excel
    user_dict.to_excel('Storage.xlsx', index=False)
    start()

admin()

