

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('sqlite:///sortinghat.db')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())

    results = relationship('Result', back_populates='user')

class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer(), primary_key=True)
    housename = Column(String())

    results = relationship('Result', back_populates='house')

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
    question1 = Column(Integer())
    question2 = Column(Integer())
    question3 = Column(Integer())
    question4 = Column(Integer())
    question5 = Column(Integer())
    question6  = Column(Integer())
    house_id = Column(Integer(), ForeignKey('houses.id'))

    user = relationship('User', back_populates='results')
    house = relationship('House', back_populates='results')

class Question(Base):
    __tablename__ = 'questions'

    id = Column(Integer(), primary_key=True)
    question = Column(String())
    answer_a = Column(String())
    answer_b = Column(String())
    value_a = Column(Integer())
    value_b = Column(Integer())
    value_c = Column(Integer())
