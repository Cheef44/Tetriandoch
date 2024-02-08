import sqlite3
from Crypto.Hash import SHA3_512

#Класс создания базы данных пользователя
class DataBase:
    #Инициализация класса
    def __init__(self, password, username) -> None:
        hash_password = SHA3_512.new(bytes(password, 'utf-8')).digest()
        hash_username = SHA3_512.new(bytes(username, 'utf-8')).digest()
        self.password = hash_password
        self.username = hash_username
    
    #Проверка регистарции
    def check_db(self):
        try:
            with sqlite3.connect('database.db') as conn:
                cursor = conn.cursor()
                user_name = cursor.execute("""SELECT user_name FROM user""").fetchall()
                if user_name:
                    return True
                else:
                    return False
        except sqlite3.OperationalError:
            return False
    
    #Создание базы данных
    def create_db(self):
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS user(
                user_name TEXT,
                password TEXT);
            """)
            
            if not self.check_db():
                cursor.execute("INSERT INTO user(user_name, password) VALUES(?, ?);", (self.username, self.password))
                cursor.close()
                conn.commit()
                return 'You have successfully registered'
            else:
                return 'You have already been registered'
    
    #Метод регистрации
    def log_in_db(self):
        login_check = False
        with sqlite3.connect('database.db') as conn:
            cursor = conn.cursor()
            if self.check_db():
                user_name = cursor.execute("""SELECT user_name FROM user;""").fetchall()
                user_password = cursor.execute("""SELECT password FROM user;""").fetchall()
                if str(*user_name[0]) == str(self.username):
                    if str(*user_password[0]) == str(self.password):
                        login_check = True
                    else:
                        login_check = False
            cursor.close()
        return login_check