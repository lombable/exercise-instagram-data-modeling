import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), unique=True, nullable=False)
    first_name = Column(String(250), unique=False, nullable=False)
    last_name = Column(String(250), unique=False, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    comment_id = Column(Integer, ForeignKey('comment.id'))
    user_from_id = Column(Integer, ForeignKey('follower.id'))
    user_to_id = Column(Integer, ForeignKey('follower.id'))
    direct_message = Column(String(500))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    comment_id = Column(Integer, ForeignKey('comment.id'))
    media_id = Column(Integer, ForeignKey('media.id'))


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type_media = Column(Enum, unique=False, nullable=False)
    url = Column(String(250), unique=False, nullable=False)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), unique=False, nullable=False)
    
class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)

class DM(Base):
    __tablename__ = 'DMs'
    id = Column(Integer, primary_key=True)
    direct_message = Column(String(500), ForeignKey('user.direct_message'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e