#!/usr/bin/python3
"""Square class inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class """
    def __init__(self, size, x=0, y=0, id=None):
        super.__init__(size, size, x, y, id)

    def __str__(self):
        """override method"""
        return 'f[Square] (<self.id>) <self.x>/<self.y> - <self.width>'

    @property
    def size(self):
        """Getter function for the  attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter function for the  attribute size"""
        if not isinstance(self.__width, int):
            raise TypeError("width must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def update(self, *args, **kwargs):
        """updste function"""
        if args != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """to dictionary method"""
        dict = {
            "id": self.id,
            "size": self.__width,
            "x": self.__x,
            "y": self.__y
            }
        return dict
