import sqlite3
from database_connection import get_database_route
db = get_database_route()


class User_repo:

    def __init__(self, file):
        self._file = file
    
    def register_user(self, user):

        cursor = self._file.cursor()
        cursor.execute("INSERT INTO Users (name, password) VALUES (?, ?)", (user.name, user.password) )
        self._file.commit()
        print("moi")
        return user
        






user_repo = User_repo(db)