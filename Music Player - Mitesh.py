# This program lets users manage a music library
# Features: add songs, search songs, sort songs, display songs, albums, and artists

# Step 1: Define Classes
# ------------------------------

class LibraryItem:
    """Base class for library items"""
    def __init__(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title

class Song(LibraryItem):
    """Represents a Song"""
    def __init__(self, title, artist, album, genre, duration):
        super().__init__(title)
        self.artist = artist
        self.album = album
        self.genre = genre
        self.duration = duration

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.album})"

class Album(LibraryItem):
    """Represents an Album"""
    def __init__(self, title, artist):
        super().__init__(title)
        self.artist = artist
        self.songs = []          # List of songs in this album

    def add_song(self, song):
        self.songs.append(song)

    def get_songs(self):
        return self.songs

class Artist(LibraryItem):
    """Represents an Artist"""
    def __init__(self, name):
        super().__init__(name)
        self.albums = []         # List of albums created by this artist

    def add_album(self, album):
        self.albums.append(album)

    def get_albums(self):
        return self.albums
    


# Step 2: Data Storage
# We use a list to store all songs, and dictionaries for albums and artists.
# -----------------------------------------------------------------------------


songs = []       # List to store Song objects
albums = {}      # album_title -> Album object
artists = {}     # artist_name -> Artist object



# Step 3: Helper Functions
# ------------------------------

def add_song():      
    """Ask user to input song details and store it in the library"""
    title = input("Enter song title: ")
    artist_name = input("Enter artist: ")
    album_title = input("Enter album: ")
    genre = input("Enter genre: ")
    duration = input("Enter duration: ")

    # Create a new Song object and add it to the songs list
    song = Song(title, artist_name, album_title, genre, duration)
    songs.append(song)

    # Add album if not exists
    if album_title not in albums:
        albums[album_title] = Album(album_title, artist_name)
    albums[album_title].add_song(song)

    # Add artist if not exists 
    if artist_name not in artists:
        artists[artist_name] = Artist(artist_name)
    if albums[album_title] not in artists[artist_name].get_albums():
        artists[artist_name].add_album(albums[album_title])

    print(f"\n Added song: {song}\n")

def display_songs():
    """Display all songs in the library"""
    if not songs:
        print("No songs in the library.\n")
        return
    print("\n--- All Songs ---")
    for i, song in enumerate(songs, 1):
        print(f"{i}. {song}")
    print()

def display_albums():
    """Display all albums in the library"""
    if not albums:
        print("No albums in the library.\n")
        return
    print("\n--- Albums ---")
    for album in albums.values():
        print(f"{album.title} by {album.artist}, Songs: {[s.title for s in album.get_songs()]}")
    print()

def display_artists():
    """Display all artists in the library"""
    if not artists:
        print("No artists in the library.\n")
        return
    print("\n--- Artists ---")
    for artist in artists.values():
        print(f"{artist.title}, Albums: {[a.title for a in artist.get_albums()]}")
    print()

def search_song():
    """Search for a song by title"""
    query = input("Enter song title to search: ").lower()
    found = [s for s in songs if query in s.get_title().lower()]
    if found:
        print("\n--- Search Results ---")
        for s in found:
            print(s)
    else:
        print("No songs found with that title.")
    print()

def sort_songs():
    """Sort songs alphabetically by title"""
    songs.sort(key=lambda s: s.get_title().lower())
    print("✅ Songs sorted alphabetically by title.\n")



# Step 4: Add Default Songs
# ------------------------------

def add_default_songs():
    """I load 11 default songs into the library at startup"""

    defaults = [
        ("Shape of You", "Ed Sheeran", "Divide", "Pop", "3:53"),
        ("Blinding Lights", "The Weeknd", "After Hours", "Synthpop", "3:20"),
        ("Someone Like You", "Adele", "21", "Soul", "4:45"),
        ("Let Her Go", "Passenger", "All the Little Lights", "Folk", "4:12"),
        ("Counting Stars", "OneRepublic", "Native", "Pop Rock", "4:17"),
        ("Senorita", "Shawn Mendes", "SM2", "Pop", "3:10"),
        ("Perfect", "Ed Sheeran", "Divide", "Pop", "4:23"),
        ("Believer", "Imagine Dragons", "Evolve", "Rock", "3:24"),
        ("Rolling in the Deep", "Adele", "21", "Soul", "3:48"),
        ("Closer", "The Chainsmokers", "Collage", "EDM", "4:04"),
        ("Levitating", "Dua Lipa", "Future Nostalgia", "Pop", "3:23")
    ]
    for t, a, al, g, d in defaults:
        song = Song(t, a, al, g, d)
        songs.append(song)
        if al not in albums:
            albums[al] = Album(al, a)
        albums[al].add_song(song)
        if a not in artists:
            artists[a] = Artist(a)
        if albums[al] not in artists[a].get_albums():
            artists[a].add_album(albums[al])



# Step 5: Main Menu
# ------------------------------

def main_menu():
    """Main menu loop for user interaction"""
    add_default_songs()
    while True:
        print("=== Music Library Menu ===")
        print("1. Display all songs")
        print("2. Display albums")
        print("3. Display artists")
        print("4. Add a new song")
        print("5. Search a song")
        print("6. Sort songs by title")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            display_songs()
        elif choice == "2":
            display_albums()
        elif choice == "3":
            display_artists()
        elif choice == "4":
            add_song()
        elif choice == "5":
            search_song()
        elif choice == "6":
            sort_songs()
        elif choice == "0":
            print("Goodbye! 🎵")
            break
        else:
            print("Invalid choice, try again.\n")

# ===============================
# Run the program
# ===============================

if __name__ == "__main__":
    main_menu()