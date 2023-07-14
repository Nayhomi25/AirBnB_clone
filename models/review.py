#!/usr/bin/python3
"""Defines the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent an amenity.
    Attributes:
        place_id(str): The Place.id
        user_id(str): The User.id
        text(str): string
    """
    place_id = ""
    user_id = ""
    text = ""
