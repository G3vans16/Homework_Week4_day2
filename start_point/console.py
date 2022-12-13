# Use this file to test your repository functions 
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# delete contents of album table
# delete contents of artists table
album_repository.delete_all()
artist_repository.delete_all()


artist1 = Artist("Foo Fighters")
artist_repository.save(artist1)
artist2 = Artist("Muse")
artist_repository.save(artist2)

# artist1.id = 3

album1 = Album("The Colour and The Shape", artist1)
album_repository.save(album1)
album2 = Album("Absolution", artist2)
album_repository.save(album2)