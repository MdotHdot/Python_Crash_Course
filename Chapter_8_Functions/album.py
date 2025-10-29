#using deful values return values and a dictionary entry creat create a function that wil enter albums badsed on artists into a dictionary
def make_album(artist, album, tracks=None):
    """Return a dictionary representing an album."""
    album_info = {
        'artist': artist,
        'album': album
    }
    if tracks:
        album_info['tracks'] = tracks
    return album_info
while True:
    print("\nPlease enter the album details:")
    print("(enter 'q' at any time to quit)")

    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break

    album = input("Album name: ")
    if album.lower() == 'q':
        break

    tracks = input("Number of tracks (optional, press Enter to skip): ")
    if tracks.lower() == 'q':
        break
    elif tracks:
        tracks = int(tracks)

    album_info = make_album(artist, album, tracks)
    print(f"\nAlbum information: {album_info}")
    

# make_album('Taylor Swift', '1989')
# make_album('Adele', '25', tracks=11)
# # Example usage
# album1 = make_album('The Beatles', 'Abbey Road')
# album2 = make_album('Pink Floyd', 'The Dark Side of the Moon', tracks=10)
# print(album1)  # Output: {'artist': 'The Beatles', 'album': 'Abbey Road'}
# print(album2)  # Output: {'artist': 'Pink Floyd', 'album': 'The Dark Side of the Moon', 'tracks': 10}
# # This will use the function to create an album
# album3 = make_album('Nirvana', 'Nevermind', tracks=12)

