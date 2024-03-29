#!/usr/bin/python3
"""
Rectangle Module
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Get rectangle width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set rectangle width.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Get rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set rectangle height.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Get x coordinator of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set x coordinator of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Get y coordinator of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set y coordinator of the rectangle.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        return the area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character '#'.
        """
        # Check if the rectangle has no area
        if self.width == 0 or self.height == 0:
            print("")
            return
        # Print the top margin (y-axis offset)
        for _ in range(self.y):
            print("")

        # Print the rectangle
        for h in range(self.height):
            # Print the left margin (x-axis offset)
            print(" " * self.x, end="")

            # Print the rectangle row
            print("#" * self.width)

    def update(self, *args, **kwargs):
        """
        Update the properties of the Rectangle instance.
        """
        attributes = ['id', 'width', 'height', 'x', 'y']

        # Update using positional arguments
        if args:
            for i, arg in enumerate(args):
                # Ensure the index is within the attributes
                if i < len(attributes):
                    if arg is None and i == 0:
                        # Reset to initial values if 'id' is None
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        setattr(self, attributes[i], arg)

        # Update using keyword arguments
        elif kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    if key == 'id' and value is None:
                        # Reset to initial values if 'id' is None
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of a Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return to this format: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        message = (
            f"[Rectangle] ({self.id}) {self.x}/{self.y}"
            f" - {self.width}/{self.height}"
        )
        return message
