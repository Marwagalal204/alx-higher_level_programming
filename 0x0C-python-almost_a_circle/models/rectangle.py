#!/usr/bin/python3
"""Define a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rectangle  class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter function for the private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for the private attribute width"""
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if type(value) is not int:
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
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

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
