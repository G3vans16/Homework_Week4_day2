# Use this file to test your repository functions 
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# delete contents of album table
# delete contents of artists table


artist1 = Artist("Foo Fighters")
# artist_repository.save(artist1)

artist1.id = 3

album1 = Album("The Colour and The Shape", artist1)
album_repository.save(album1)