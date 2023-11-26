#!/usr/bin/python3
"""
11. Student to disk and reload
"""


class Student:
    """
    Class Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, selected_attributes=None):
        """
        Convert to Json with filter
        """
        if isinstance(selected_attributes, list):
            result = {}
            for attribute in selected_attributes:
                if isinstance(attribute, str) and hasattr(self, attribute):
                    result[attribute] = getattr(self, attribute)
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
