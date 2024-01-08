#!/usr/bin/python3
"""
Square Module
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor for Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Get square size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Set square size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the properties of the Square instance.
        """
        # Define attribute names in order
        attributes = ['id', 'size', 'x', 'y']

        # Update using positional arguments
        if args:
            for index, arg in enumerate(args):
                if index < len(attributes):  # Check if index is valid
                    if arg is None and index == 0:
                        # Reset to initial values if 'id' is None
                        self.__init__(self.size, self.x, self.y)
                    else:
                        setattr(self, attributes[index], arg)

        # Update using keyword arguments
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    if key == 'id' and value is None:
                        # Reset to initial values if 'id' is None
                        self.__init__(self.size, self.x, self.y)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return to this format: [Square] (<id>) <x>/<y> - <size
        """
        message = (
            f"[Square] ({self.id}) {self.x}/{self.y}"
            f" - {self.width}"
        )
        return message
