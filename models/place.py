#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(
        String(60), ForeignKey('cities.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    user_id = Column(
        String(60), ForeignKey('users.id'), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    description = Column(
        String(1024)
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    number_rooms = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    number_bathrooms = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    max_guest = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    price_by_night = Column(
        Integer, nullable=False, default=0
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    latitude = Column(
        Float
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    longitude = Column(
        Float
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    amenity_ids = []
    user = relationship(
            'User',
            back_populates='places'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    cities = relationship(
            'City',
            back_populates='places'
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
                'Review',
                cascade='all, delete, delete-orphan',
                back_populates='place'
        )
    else:
        @property
        def reviews(self):
            """returns the list of Review instances
            of specific place
            """
            from models import storage
            from model.review import Review
            reviews_objs = []
            for v in storage.all(Review).values():
                if v.id == self.place_id:
                    reviews_objs.append(v)
            return reviews_objs
