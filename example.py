from __future__ import print_function
from tmdb_wrapper import TV

popular = TV.popular()
info = TV.info
# print(info(1403))

for number, show in enumerate(popular['results'], start=1):
    print("{}. {} - {}".format(
        number, show['name'], show['popularity']))
