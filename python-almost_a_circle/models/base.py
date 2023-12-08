#!/usr/bin/python3
"""
Base Module
"""


import json


class Base:
    """
    Base Class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON serialization of a list of dicts.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON serialization of a list of objects to a file.
        """
        # Define the filename based on the class name
        filename = f"{cls.__name__}.json"

        # Open the file for writing
        with open(filename, "w") as jsonfile:
            # Check if the list of objects is empty or None
            if not list_objs:
                # Write an empty JSON array to the file
                jsonfile.write("[]")
            else:
                # Convert each object in the list to its dictionary representation
                list_dicts = [obj.to_dictionary() for obj in list_objs]

                # Serialize the list of dictionaries to a JSON string and write to the file
                jsonfile.write(Base.to_json_string(list_dicts))
