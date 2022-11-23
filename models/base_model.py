#!/usr/bin/python3
""" Module for storing the BaseModel class. """
from datetime import datetime
import models
from uuid import uuid4


class BaseModel():
    """ BaseModel class for handling base attributes."""
    # __init__ | Private | method |-------------------------------------------|
    def __init__(self, *args, **kwargs):
        """ Initializtion for the BaseModel class object. """
        if kwargs:
            for key in kwargs.keys():
                time = '%Y-%m-%dT%H:%M:%S.%f'
                if key == "__class__":
                    continue
                else:
                    if key == "created_at":
                        self.created_at = datetime.strptime(kwargs[key], time)
                    elif key == "updated_at":
                        self.updated_at = datetime.strptime(kwargs[key], time)
                    else:
                        setattr(self, key, kwargs[key])
         else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    # save | Public | method |------------------------------------------------|
    def save(self):
        """ Sets the updated_at time for the current time """
        self.updated_at = datetime.today()
        models.storage.save()

    # to_dict | Public | method |---------------------------------------------|
    def to_dict(self):
        """Returns a dict representation of object-instance"""
        list_of_attributes = []
        dicto_final = {}

        # Uncomment lines below to add default attributes as well.
        # for name in dir(self):
        #     if name[0] != '_' and name != "to_dict" and name != "save":
        #         list_of_attributes.append(name)

        # For every attribute in the __dict__.
        for attribute in self.__dict__:
            # If attribute doesn't begin with a "_" character.
            if attribute[0] != '_':
                # Append the name of the attribute to the list.
                list_of_attributes.append(attribute)
        # Append __class__
        list_of_attributes.append('__class__')

        # for every attribute in the list.
        for attribute in list_of_attributes:

            # Set appropiate isoformat.
            if attribute == "created_at":
                dicto_final[attribute] = self.created_at.isoformat("T")

            # Set appropiate isoformat.
            elif attribute == "updated_at":
                dicto_final[attribute] = self.updated_at.isoformat("T")

            # Set class name as __name__.
            elif attribute == "__class__":
                dicto_final[attribute] = self.__class__.__name__

            # Else get value of the attributes.
            else:
                # Add that value to the dictionary.
                dicto_final[attribute] = getattr(self, attribute)
                # Uncomment two lines below to add default attributes as well.
                # string = "self.{}".format(attribute)
                # dicto_final[attribute] = eval(string)
        return (dicto_final)

    # __str__ | Private | method |--------------------------------------------|
    def __str__(self):
        """ Returns the string representation of the BaseModel object. """
        string = "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            str(self.__dict__))
        return string