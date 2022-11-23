#!/usr/bin/python3
""" Module for storing and reload from JSON file"""
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from models.city import City
import json


class FileStorage():
    """
    FileStorage class for handling serialization and deserialization of objects
    on a JSON format, and managing the file.json for persistance over sessions.
    """
    __file_path = 'file.json'
    __objects = {}

    # all | Public | method |-------------------------------------------------|
    def all(self):
        """Returns dict stored in __objects"""
        return self.__objects

    # new | Public | method |-------------------------------------------------|
    def new(self, obj):
        '''
        Creates a new instance of a object, and stores in public
        __objects

        Args:
            obj: new instance object to create
        '''
        key = "{}.{}".format(obj.__class__.__name__, obj.id)  # Classname.id
        self.__objects[key] = obj  # Store Object

    # save | Public | method |------------------------------------------------|
    def save(self):
        """
        Save content of our multi dict __objects, in JSON format
        on a <file.json>
        """
        dicto = {}
        for key, obj in self.__objects.items():
            dicto[key] = obj.to_dict()

        with open(self.__file_path, "w") as f:
            json.dump(dicto, f)

    # reload | Public | method |----------------------------------------------|
    def reload(self):
        """
        Load JSON content of <file.json>, in multi dict format on
        __objects
        """
        try:
            with open(self.__file_path, "r") as f:
                self.__objects = json.loads(f.read())

                for obj_id, obj in self.__objects.items():
                    self.__objects[obj_id] = eval(obj['__class__'])(**obj)

        except FileNotFoundError:
            pass

    # delete | Public | method | Custom made method --------------------------|
    def delete(self, class_name="", class_id=""):
        """ Deletes an instance currently stored"""
        switch = False
        string = class_name + "." + class_id

        for obj_id, obj in self.__objects.items():
            if string == obj_id:
                self.__objects.pop(string)
                self.save()
                switch = True
                return True

        if switch is False:
            return False

    # update | Public | method | Custom made method --------------------------|
    def update(self, obj_id, key, value):
        '''
        Updates our multi dict __objects, with id of instance to modify
        
        Args:
            obj_id: instance id to modify
            key: Attribute of instance
            value: value of attribute
        '''
        try:
            if key != "updated_at" and key != "created_at" and key != "id":
                switch = True

                # List of string attributes.
                str_attributes = ["name", "state_id", "city_id", "user_id",
                                  "description", "place_id", "text"]
                for name in str_attributes:
                    if key == name:
                        switch = True
                        value = str(value)
                        break

                # List of integer attributes.
                int_attributes = ["number_rooms", "number_bathrooms",
                                  "max_guest", "price_by_night"]
                # Compare given attribute with integer attributes
                for name in int_attributes:
                    # If name of the attribute is correct
                    if key == name:
                        # Try casting to int
                        try:
                            switch = True
                            value = int(value)
                            break
                        except ValueError:
                            print("*** Dont be silly cannot cast "
                                  "<{}> to int ***".format(value))
                            switch = False

                # List of floating point attributes.
                float_attributes = ["latitude", "longitude"]
                # Compare given attribute with float attributes
                for name in float_attributes:
                    # If name of the attribute is correct
                    if key == name:
                        # Try casting to float
                        try:
                            switch = True
                            value = float(value)
                            break
                        except ValueError:
                            print("*** Dont be silly cannot cast "
                                  "<{}> to float ***".format(value))
                            switch = False

                # Set the given attribute by key:value pair.
                if switch is True:
                    setattr(self.__objects[obj_id], key, value)
                    self.save()
                    return True

        # Except no ClassName.id found on the dictionary
        except KeyError:
            return False