#!/usr/bin/python3
"""Define a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle  class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter function for the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for the private attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter function for the private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for the private attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter function for the private attribute x"""
        return self.__x

    @x.setter
    def x(self,  value):
        """Setter function for the private attribute x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter function for the private attribute y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function for the private attribute y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculate the Rectangle Area"""
        return self.__height * self.__width

    def display(self):
        """dispaly Rectangle area by symbol #"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for n in range(self.__y):
            print()
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """override method"""
        msg = (f'[Rectangle] ({self.id}) '
               f'{self.__x}/{self.__y} - {self.width}/{self.height}')
        return msg

    def update(self, *args, **kwargs):
        """update method"""
        if args != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """to dictionary method"""
        dict = {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
            }
        return dict
