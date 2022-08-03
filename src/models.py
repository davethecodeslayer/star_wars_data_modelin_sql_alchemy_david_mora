import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(30), nullable=False, unique=True)
    suscription_date = Column(String(20), nullable=False)
    suscription_plan = Column(String(20), nullable=False)
    favorites = relationship('Favorites')

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    character_id = Column(Integer, ForeignKey("character.id"))
    starship_id = Column(Integer, ForeignKey("starship.id"))
    planet_id = Column(Integer, ForeignKey("planet.id"))
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    birth_year = Column(Integer, nullable=False)
    eye_color = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    skin_color = Column(String(100), nullable=False)
    species = Column(String(100), nullable=False)
    starships = Column(Integer, nullable=False)
    favorites = relationship('Favorites')
    homeplanet = Column(Integer, ForeignKey("planet.id"))


class Starships(Base):
    __tablename__= 'starship'
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(Integer, nullable=False)
    name  = Column(String(100), nullable=False, unique=True)
    favorites = relationship('Favorites')

class Planets(Base):
    __tablename__= 'planet'
    id = Column(Integer, primary_key=True)
    climate = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    favorites = relationship('Favorites')
    citizens = relationship('Character')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
