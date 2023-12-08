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
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Return the deserialization of a JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instantied from a dictionary of attributes.
        """
        if dictionary:
            # Create a new instance based on the class name
            if cls.__name__ == "Rectangle":
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)

            new_instance.update(**dictionary)

            return new_instance

    @classmethod
    def load_from_file(cls):
        """
        Return a list of classes instantiated from a file of JSON strings.
        """
        filename = f"{cls.__name__}.json"

        try:
            # Open the file and read its contents
            with open(filename, "r") as jsonfile:
                # Deserialize the JSON string into a list of dictionaries
                list_dicts = Base.from_json_string(jsonfile.read())

                # Create and return a list of class instances from the dictionaries
                return [cls.create(**dict_obj) for dict_obj in list_dicts]
        except IOError:
            # Return an empty list if the file cannot be opened or read
            return []
