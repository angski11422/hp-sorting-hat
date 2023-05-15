

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///sortinghat.db')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())

class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer(), primary_key=True)
    housename = Column(String())

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    house_id = Column(Integer(), ForeignKey('houses.id'))
