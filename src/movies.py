class AdamSandlerMovie(object):
    def __init__(self, title):
        self.title = title

class GoodAdamSandlerMovie(AdamSandlerMovie):
    def __init__(self, *args, **kwargs):
        raise NotImplementedError()

class BadAdamSandlerMovie(AdamSandlerMovie):
    pass


MOVIES = [
    {"title": "Billy Madison", "year": 1995, "category": "good"},
    {"title": "Happy Gilmore", "year": 1996, "category": "good"},
    {"title": "The Wedding Singer", "year": 1998, "category": "good"},
    {"title": "The Waterboy", "year": 1998, "category": "good"},
    {"title": "Big Daddy", "year": 1999, "category": "good"},
    {"title": "Punch-Drunk Love", "year": 2002, "category": "good"},
    {"title": "50 First Dates", "year": 2004, "category": "good"},
    {"title": "Click", "year": 2006, "category": "good"},
    {"title": "Funny People", "year": 2009, "category": "good"},
    {"title": "Uncut Gems", "year": 2019, "category": "good"},
    {"title": "Hustle", "year": 2022, "category": "good"},
    {"title": "Jack and Jill", "year": 2011, "category": "bad"},
    {"title": "That's My Boy", "year": 2012, "category": "bad"},
    {"title": "Grown Ups 2", "year": 2013, "category": "bad"},
    {"title": "Pixels", "year": 2015, "category": "bad"},
    {"title": "The Ridiculous 6", "year": 2015, "category": "bad"},
    {"title": "The Do-Over", "year": 2016, "category": "bad"},
    {"title": "Sandy Wexler", "year": 2017, "category": "bad"},
]


def get_movies():
    return MOVIES


def get_good_movies():
    return [m for m in MOVIES if m["category"] == "good"]


def get_bad_movies():
    return [m for m in MOVIES if m["category"] == "bad"]
