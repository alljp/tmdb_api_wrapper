from . import session


class People(object):

    def info(id):
        path = 'https://api.themoviedb.org/3/person/{}'.format(id)
        response = session.get(path)
        return response.json()
