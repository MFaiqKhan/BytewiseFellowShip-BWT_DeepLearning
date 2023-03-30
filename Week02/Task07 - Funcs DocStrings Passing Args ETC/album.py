def make_album(artist, title, tracks=None):
    """Return a dictionary of information about an album."""
    album = {
        "artist": artist,
        "title": title,
    }
    if tracks:
        album["tracks"] = tracks
    return album


print(make_album("The Weeknd", "After Hours"))
print(make_album("The Weeknd", "After Hours", tracks=14))
print(make_album("Katy Perry", "Smile", tracks=12))	