#!/usr/bin/python3
"""Defines the City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a state.
    Attributes:
        state_id(str): the state id
        name (str): The name of the state.
    """

    state_id = ""
    name = ""
