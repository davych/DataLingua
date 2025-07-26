from db import SessionLocal, User, Artist, Album, Song, Like, init_db

def init_mock_data():
    db = SessionLocal()
    db.query(Like).delete()
    db.query(Song).delete()
    db.query(Album).delete()
    db.query(Artist).delete()
    db.query(User).delete()
    db.commit()
    user = User(name="Alice")
    db.add(user)
    artist = Artist(name="Jay Chou")
    db.add(artist)
    album = Album(title="Fantasy", artist_id=1)
    db.add(album)
    song = Song(title="Simple Love", album_id=1, artist_id=1)
    db.add(song)
    like = Like(user_id=1, song_id=1)
    db.add(like)
    db.commit()
    db.close()

if __name__ == "__main__":
    init_db()
    init_mock_data()
    print("Mock data initialized.")
