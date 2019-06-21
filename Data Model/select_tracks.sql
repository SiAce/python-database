SELECT Track.title AS Title, Album.title AS Album, Artist.name AS Artist
FROM Track JOIN Album JOIN Artist
ON Track.album_id = Album.id AND Album.artist_id = Artist.id