from __future__ import print_function
from tmdb_wrapper import TV
from tmdb_wrapper import Movie

popular = TV.popular()

print("Popular TV shows")
for number, show in enumerate(popular['results'], start=1):
    print("{}. {} - {}".format(
        number, show['name'], show['popularity']))

popular_movies = Movie.popular()
print(popular_movies)
print("\n\nPopular Movies")
for number, movie in enumerate(popular_movies['results'], start=1):
    print("{}. {} - {}".format(number, movie['title'], movie['popularity']))
