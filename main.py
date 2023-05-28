# Импортируем необходимые библиотеки
import tkinter as tk
import mysql.connector

# Создаем окно приложения
root = tk.Tk()
root.title("Школьная библиотека")

# Создаем функцию для подключения к базе данных
def connect_to_db():
    global mydb
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="school_library"
    )

# Создаем функцию для вывода данных из базы данных
def show_data():
    # Создаем курсор для работы с базой данных
    mycursor = mydb.cursor()

    # Выполняем запрос на выборку данных из таблицы
    mycursor.execute("SELECT * FROM books")

    # Получаем результаты запроса
    myresult = mycursor.fetchall()

    # Выводим результаты на экран
    for x in myresult:
        print(x)

# Создаем функцию для добавления данных в базу данных
def add_data():
    # Создаем курсор для работы с базой данных
    mycursor = mydb.cursor()

    # Выполняем запрос на добавление данных в таблицу
    sql = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
    val = ("Название книги", "Автор книги", 2021)
    mycursor.execute(sql, val)

    # Сохраняем изменения в базе данных
    mydb.commit()

    # Выводим сообщение об успешном добавлении данных
    print(mycursor.rowcount, "запись добавлена")

# Создаем функцию для удаления данных из базы данных
def delete_data():
    # Создаем курсор для работы с базой данных
    mycursor = mydb.cursor()

    # Выполняем запрос на удаление данных из таблицы
    sql = "DELETE FROM books WHERE year = 2021"
    mycursor.execute(sql)

    # Сохраняем изменения в базе данных
    mydb.commit()

    # Выводим сообщение об успешном удалении данных
    print(mycursor.rowcount, "запись удалена")

# Создаем функцию для редактирования данных в базе данных
def edit_data():
    # Создаем курсор для работы с базой данных
    mycursor = mydb.cursor()

    # Выполняем запрос на изменение данных в таблице
    sql = "UPDATE books SET title = 'Новое название книги' WHERE year = 2021"
    mycursor.execute(sql)

    # Сохраняем изменения в базе данных
    mydb.commit()

    # Выводим сообщение об успешном изменении данных
    print(mycursor.rowcount, "запись изменена")

# Создаем функцию для вывода справки
def show_help():
    # Выводим сообщение с описанием программы
    print("Школьная библиотека - это программа для управления базой данных книг в школьной библиотеке. С помощью данной программы вы можете просматривать, добавлять, удалять и редактировать данные в базе данных.")

# Создаем кнопки для работы с базой данных
connect_button = tk.Button(root, text="Подключиться к базе данных", command=connect_to_db)
show_data_button = tk.Button(root, text="Показать данные", command=show_data)
add_data_button = tk.Button(root, text="Добавить данные", command=add_data)
delete_data_button = tk.Button(root, text="Удалить данные", command=delete_data)
edit_data_button = tk.Button(root, text="Редактировать данные", command=edit_data)

# Создаем кнопку для вывода справки
help_button = tk.Button(root, text="Справка", command=show_help)

# Размещаем кнопки на экране
connect_button.pack()
show_data_button.pack()
add_data_button.pack()
delete_data_button.pack()
edit_data_button.pack()
help_button.pack()

# Запускаем главный цикл приложения
root.mainloop()