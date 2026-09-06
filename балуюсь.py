import sqlite3

#объявление бд
bd = sqlite3.connect('server.db') #база данных
sql = bd.cursor() #курсор (то с помощью чего работаем с бд)

#создание бд
sql.execute("""CREATE TABLE IF NOT EXISTS users(
            login TEXT,
            password TEXT,
            mail TEXT,
            age INT,
            gender TEXT,
            games INT,
            wins INT,
            score INT
)""")
bd.commit() #поддтверждение создания базы данных

#видео-урок
"""sql.execute("SELECT login FROM users") #выбираем столбец login
if sql.fetchone() is None:
    sql.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (log, pas, mail, age, gender))
    bd.commit() #подтверждение действия!!
    print("вы зарегестрированы")
    # '{log}', '{pas}', '{mail}', {age}, '{gender}'
else:
    print("такое уже есть")
    for value in sql.execute("SELECT * FROM users"):
        print(value)"""

#мои попытки на проверку существования в бд
"""# sql.execute("SELECT login FROM users") #выбираем столбец login
# for value in sql.fetchall():
sql.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (login, pasword, mail, age, gender))
bd.commit() #подтверждение действия!!
for value in sql.execute ("SELECT login FROM users"):
    for value2 in sql.execute ("SELECT login FROM users"):
        if value == value2:
            sql.execute(f"DELETE from users login = ?", (value2))
            bd.commit() #подтверждение действия!!"""

#удаление
"""sql.execute("DELETE from users where age = 0")
bd.commit() #подтверждение действия!!"""

#проверка на существование в бд
"""sql.execute(f"SELECT login FROM users WHERE login = '{login}'")
if sql.fetchone() is None:
    sql.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?)", (login, pasword, mail, age, gender))
    bd.commit() #подтверждение действия!!
else:
    print("уже есть")"""

#вывод
sql.execute("SELECT login FROM users") #выбираем столбец login
for value in sql.execute("SELECT * FROM users"):
    print(value)

"""sql.execute("SELECT login FROM users")
for value in sql.execute(f"SELECT login FROM users WHERE mail = '{login}'"):
    print(value)
    login = value[0]
print (login)"""

login = 'mya'

i = 1
for log in sql.execute("SELECT login FROM users ORDER BY score DESC"): #определение номера в рейтинге
    print (log)
    if "".join(log) == login:
        break   
    i += 1 #шаг

print(i)