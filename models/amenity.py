#!/usr/bin/python3
""" State Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.place import PlaceAmenity


class Amenity(BaseModel, Base):
    """represent amenities"""
    __tablename__ = 'amenities'
    name = Column(
            String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    place_amenities = relationship(
            'Place',
            secondary=PlaceAmenity,
            back_populates='amenities',
            viewonly=True
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else None
