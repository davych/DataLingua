from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    artist_id = Column(Integer, ForeignKey('artist.id'))
    artist = relationship('Artist')

class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    album_id = Column(Integer, ForeignKey('album.id'))
    artist_id = Column(Integer, ForeignKey('artist.id'))
    album = relationship('Album')
    artist = relationship('Artist')

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    song_id = Column(Integer, ForeignKey('song.id'))
    user = relationship('User')
    song = relationship('Song')

engine = create_engine('sqlite:///music.db', echo=False, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)
