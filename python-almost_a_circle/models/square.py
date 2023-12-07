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

    def __str__(self):
        """
        Return to this format: [Square] (<id>) <x>/<y> - <size
        """
        message = (
            f"[Square] ({self.id}) {self.x}/{self.y}"
            f" - {self.width}"
        )
        return message
