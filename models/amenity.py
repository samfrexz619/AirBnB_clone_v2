#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class Amenity(BaseModel, Base):
    '''
    class Amenity
    Attrs:
        name: input
    '''

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place',
                                   secondary='place_amenity',
                                   backref='amenities',
                                   cascade='delete')
