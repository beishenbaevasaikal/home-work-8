import sqlite3

# Подключаемся к базе данных (если она не существует, будет создана новая)
conn = sqlite3.connect('students.db')

# Создаем курсор для работы с базой данных
cursor = conn.cursor()

# Создаем таблицу "студент", если её нет
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY,
                    hobby TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    birth_year INTEGER,
                    homework_points INTEGER
                )''')

cursor.execute("SELECT * FROM students WHERE LENGTH(last_name) > 10")
print("Студенты у которых фамилия больше 10 символов:")
for row in cursor.fetchall():
    print(row)

# 2. Изменяем имена всех студентов у которых балл больше 10 на "genius"
cursor.execute("UPDATE students SET first_name='genius' WHERE homework_points > 10")

# 3. Выводим всех "genius"
cursor.execute("SELECT * FROM students WHERE first_name='genius'")
print("\nСтуденты со словом 'genius' в имени:")
for row in cursor.fetchall():
    print(row)

# 4. Удаляем всех студентов у которых id четное
cursor.execute("DELETE FROM students WHERE id % 2 = 0")

# Сохраняем изменения
conn.commit()

# Закрываем соединение с базой данных
conn.close()