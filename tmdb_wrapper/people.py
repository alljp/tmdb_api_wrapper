from . import session


class People(object):

    def info(id):
        path = 'https://api.themoviedb.org/3/person/{}'.format(id)
        response = session.get(path)
        return response.json()

    def movie_credits(id):
        path = 'https://api.themoviedb.org/3/person/{}/movie_credits'.format(
            id)
        response = session.get(path)
        return response.json()
