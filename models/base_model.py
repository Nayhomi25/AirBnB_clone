#!/usr/bin/python3
"""Defines the BAseModel class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the basde model of the HBNB project"""

    def __init__(self, *args, **kwargs):
        """ Initializes the BaseModel class
         Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Update the updated_at attribute with current date and time"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        sdict = self__dict__.copy()
        sdict["created_at"] = self.created_at.isoformat()
        sdict["updated_at"] = self.updated_at.isoformat()
        sdict["__class__"] = self.__class__.__name__
        return sdict

    def __str__(self):
        """Return the print/str representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
