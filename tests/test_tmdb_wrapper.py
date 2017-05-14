from tmdb_wrapper import TV


def tets_tv_info():
    tv_instance = TV(1396)
    response = tv_instance.info()

    assert isintance(response, dict)
    assert response['id'] == 1396
