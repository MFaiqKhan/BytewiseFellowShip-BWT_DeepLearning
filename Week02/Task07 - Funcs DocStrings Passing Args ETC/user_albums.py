def make_album(artist, title, tracks=None):
    """Return a dictionary of information about an album."""
    album = {
        "artist": artist,
        "title": title,
    }
    if tracks:
        album["tracks"] = tracks
    return album

while True:
    artist_name = input("Enter the artist name: ")
    if artist_name == "q":
        break
    album_name = input("Enter the album name: ")
    if album_name == "q":
        break
    tracks = input("(Optional)Enter the number of tracks: ")
    if tracks:
        album = make_album(artist_name, album_name, tracks)
    else:
        album = make_album(artist_name, album_name)

    print(album)




