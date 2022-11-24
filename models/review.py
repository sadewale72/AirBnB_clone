#!/usr/bin/python3
''' Module for storing Review class definition. '''
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Review class with place_id, user_id and the text.
    
    Attributes:
        place_id (str): place_id from review
        user_id (str): user_id who wrote the review
        text (str): message of review
    '''

    place_id = ""
    user_id = ""
    text = ""