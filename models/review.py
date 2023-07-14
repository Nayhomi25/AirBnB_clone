#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent an amenity.
    Attributes:
        name (str): The name of the amenity.
        user_id(str): The User.id
        text(str): string
    """
    name = ""
    user_id = ""
    text = ""
