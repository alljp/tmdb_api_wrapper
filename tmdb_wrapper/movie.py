from . import session


class Movie(object):

    # def __init__(self, id):
    #     self.id = id

    def info(id):
        path = 'https://api.themoviedb.org/3/movie/{}'.format(id)
        # path = 'https://api.themoviedb.org/3/tv/1403'
        response = session.get(path)
        return response.json()

    def popular():
        path = 'https://api.themoviedb.org/3/movie/popular&page=2'
        response = session.get(path)
        return response.json()
