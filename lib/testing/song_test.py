from song import Song

def test_song_class():
    # Creating some Song instances
    song1 = Song("99 Problems", "Jay-Z", "Rap")
    song2 = Song("Halo", "Beyonce", "Pop")
    song3 = Song("In the End", "Linkin Park", "Rock")
    song4 = Song("Crazy in Love", "Beyonce", "Pop")

    # Asserting the count of songs
    assert Song.count == 4

    # Asserting the list of genres
    assert Song.genres == ["Rap", "Pop", "Rock"]

    # Asserting the list of artists
    assert Song.artists == ["Jay-Z", "Beyonce", "Linkin Park"]

    # Asserting the genre count
    assert Song.genre_count == {"Rap": 1, "Pop": 2, "Rock": 1}

    # Asserting the artist count
    assert Song.artist_count == {"Jay-Z": 1, "Beyonce": 2, "Linkin Park": 1}

if __name__ == "__main__":
    test_song_class()
    print("All tests passed!")
