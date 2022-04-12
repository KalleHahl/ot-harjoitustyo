
from entities.movie import Movie
from entities.user import User
from repot.user_repo import (user_repo as default_user_repo)
from database_connection import get_database_route
db = get_database_route()

class App:

    def __init__(self, ):
        self.user = None
        self._user_repo = default_user_repo
        self._user = None
    
    def add_movie(self, movie):

        film = Movie(movie)
        return film

    def register_user(self, name, password, login=True):
        user = self._user_repo.register_user(User(name, password))
        if login:
            self._user = user

        return user



app = App()

