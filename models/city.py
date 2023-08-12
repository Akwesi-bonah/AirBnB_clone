#!/usr/bin/env python3
"""city classes that inherit from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """ class city
    attribute:
            state_id: string - empty string
            name: string - empty string
    """

    state_id = ""
    name = ""
