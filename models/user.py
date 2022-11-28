#!/usr/bin/python3
''' Module for storing User Class definition. '''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    User class with email, password, first and last name.
    
    Attributes:
        email (str): Email of user
        password (str): Password for user
        first_name (str): First name of our given user
        last_name (str): Last name of our given user
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""