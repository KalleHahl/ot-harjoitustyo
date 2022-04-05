class Movie:

    def __init__(self, name, director=None, screenplay_by=None, cinematographer=None, watched=False, user=None, movie_id=None):
        self.name = name
        self.director = director
        self.screenplay_by = screenplay_by
        self.cinematographer = cinematographer
        self.watched = watched
        self.user = user
        self.id = movie_id