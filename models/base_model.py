#!/usr/bin/python3
"""
BaseModel module for the AirBnB clone project
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self):
        """Initializes a new instance of BaseModel"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        """
        Updates the instance's update_at attribute to the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance
        """
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary

    def __str__(self):
        """
        String representation of the BaseModel class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
