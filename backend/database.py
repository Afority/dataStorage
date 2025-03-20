import psycopg2

from collections.abc import Mapping, Sequence
from typing import Any

class Db():
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname="dataStorage",
            user="almas",
            password="Almas_1337",
            host="localhost",
            port="5432"
        )

        self.cursor = self.connection.cursor()
    
    def execute(self, text, args: Sequence[Any] | Mapping[str, Any] | None = None):
        self.cursor.execute(text, args)
        try:
            return self.cursor.fetchall()
        except:
            ...

    def insert(self, table: str, colums: list, values: list):
        request: str = f"insert into {table} ("
        
        for column in colums:
            request += column + ","

        request = request.rstrip(",")

        request += ") values ("

        for value in values:
            request += "%s,"

        request = request.rstrip(",")
        request += ");"

        # insert into (%s) values (%s);
        print(request, (*colums, *values,))

        return self.execute(request, (*values,))

    def __del__(self):
        self.connection.commit()
        
dataBase = Db()
# dataBase.insert("users", 
#                 ["login", "password", "encryption_key"], 
#                 ["Almas", "pwd", "123"])
# dataBase.insert("table", ["login", "password"], ["admin", "adminLox"])
# dataBase.select("users", ["id", "login"])
# dataBase.execute("""
# CREATE TABLE files (
#     id SERIAL PRIMARY KEY,
#     client_filename VARCHAR(255) NOT NULL,
#     server_filename TEXT NOT NULL,
#     owner_id INT REFERENCES users(id) ON DELETE CASCADE
# );
# """)

# dataBase.cursor.execute("""
# CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     login VARCHAR(255) NOT NULL UNIQUE,
#     password VARCHAR(255) NOT NULL,
#     encryption_key TEXT NOT NULL
# );

# CREATE TABLE files (
#     id SERIAL PRIMARY KEY,
#     client_filename VARCHAR(255) NOT NULL,
#     server_filename TEXT NOT NULL,
#     owner_id INT REFERENCES users(id) ON DELETE CASCADE
# );

# CREATE TABLE file_access (
#     file_id INT REFERENCES files(id) ON DELETE CASCADE,
#     user_id INT REFERENCES users(id) ON DELETE CASCADE,
#     PRIMARY KEY (file_id, user_id)
# );

# CREATE TABLE sessions (
#     user_id INT REFERENCES users(id) ON DELETE CASCADE,
#     token VARCHAR(32) NOT NULL,
#     last_visit TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     useragent TEXT,
#     ip VARCHAR(45),
#     PRIMARY KEY (user_id, token)
# );
# """)

# Выполняем SQL-запрос

# dataBase = Db()
# dataBase.cursor.execute("delete from sessions;")
print(dataBase.cursor.execute("select * from users;"))
# dataBase.connection.commit()
# print(dataBase.cursor.fetchall())
