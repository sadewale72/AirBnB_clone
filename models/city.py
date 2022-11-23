#!/usr/bin/python3
''' Module for storing City Class definition. '''
from models.base_model import BaseModel


class City(BaseModel):
    '''
    City class with name and state_id.
    
    Attributes:
        state_id (str) = state_id to which it belongs
        name (str) = name of City
    '''

    state_id = ""
    name = ""