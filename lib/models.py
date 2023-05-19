

from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, func
from sqlalchemy.orm import relationship, backref, declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///sortinghat.db')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer(), primary_key=True)
    username = Column(String())

    results = relationship('Result', back_populates='user')

    def __repr__(self):
        return f"{self.id}"

class House(Base):
    __tablename__ = 'houses'

    id = Column(Integer(), primary_key=True)
    housename = Column(String())

    results = relationship('Result', back_populates='house')
    def __repr__(self):
        return f"{self.id} {self.housename}"

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.id'))
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
    value_d = Column(Integer())

    def __repr__(self):
        return f"{self.question} \n" \
            + f"a. {self.answer_a} \n" \
            + f"b. {self.answer_b} \n" \
            + "c. Neither \n" \
            + "d. Either/Both \n"

