import random
from db import SessionLocal, User, Artist, Album, Song, Like, init_db

def random_name(prefix):
    return f"{prefix}_{random.randint(1000, 9999)}"

def populate_bulk_data(n=50):
    init_db()
    db = SessionLocal()
    # 创建用户
    users = [User(name=random_name("user")) for _ in range(n)]
    db.add_all(users)
    db.flush()
    # 创建歌手
    artists = [Artist(name=random_name("artist")) for _ in range(n)]
    db.add_all(artists)
    db.flush()
    # 创建专辑
    albums = []
    for artist in artists:
        for _ in range(random.randint(1, 3)):
            albums.append(Album(title=random_name("album"), artist_id=artist.id))
    db.add_all(albums)
    db.flush()
    # 创建歌曲
    songs = []
    for album in albums:
        for _ in range(random.randint(1, 5)):
            songs.append(Song(title=random_name("song"), album_id=album.id, artist_id=album.artist_id))
    db.add_all(songs)
    db.flush()
    # 创建喜欢
    all_song_ids = [song.id for song in songs]
    for user in users:
        liked = random.sample(all_song_ids, k=min(10, len(all_song_ids)))
        for song_id in liked:
            db.add(Like(user_id=user.id, song_id=song_id))
    db.commit()
    db.close()
    print(f"Mocked {n} users, {n} artists, {len(albums)} albums, {len(songs)} songs, likes added.")

if __name__ == "__main__":
    populate_bulk_data(50)
