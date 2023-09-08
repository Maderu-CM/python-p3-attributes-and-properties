class Song:
    # Class attributes
    count = 0  # To keep track of the total number of songs created
    genres = []  # To store unique genres
    artists = []  # To store unique artists
    genre_count = {}  # To store the count of songs per genre
    artist_count = {}  # To store the count of songs per artist

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre

        # Increment the total song count
        Song.count += 1

        # Add the genre to the list of genres if it's unique
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Add the artist to the list of artists if it's unique
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Update the genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update the artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1

# Example usage
if __name__ == "__main__":
    # Create some song instances
    song1 = Song("Song 1", "Artist A", "Pop")
    song2 = Song("Song 2", "Artist B", "Rock")
    song3 = Song("Song 3", "Artist A", "Pop")

    # Print song attributes
    print(song1.name)    # Should print "Song 1"
    print(song1.artist)  # Should print "Artist A"
    print(song1.genre)   # Should print "Pop"

    # Print class attributes
    print(Song.count)      # Should print 3 (total number of songs created)
    print(Song.genres)     # Should print ["Pop", "Rock"] (unique genres)
    print(Song.artists)    # Should print ["Artist A", "Artist B"] (unique artists)

    # Print genre count
    print(Song.genre_count)  # Should print {"Pop": 2, "Rock": 1} (number of songs per genre)

    # Print artist count
    print(Song.artist_count)  # Should print {"Artist A": 2, "Artist B": 1} (number of songs per artist)
