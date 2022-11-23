#!/usr/bin/python3
''' Module for storing State Class definition. '''
from models.base_model import BaseModel


class State(BaseModel):
    '''
    State class with name.
    
    Attributes:
        name (str): name of state
    '''

    name = ""