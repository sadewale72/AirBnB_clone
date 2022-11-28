#!/usr/bin/python3
''' Module for storing Amenity class definition. '''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    Amenity class with name.
    
    Attributes:
        name (str): name of the amenities provided
    '''
    name = ""