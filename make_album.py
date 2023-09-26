def make_album(artist_name, album_title, tracks=''):
    """Return a dictionary of information about an album."""
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if tracks:
        album['tracks'] = tracks
    
    return album

album_info = make_album('eminem','encore')
print(album_info)
album2 = make_album('50 cent','the massacre', tracks = 17)
print(album2)