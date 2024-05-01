import math


class GeometricObject:
    """
    Represents a geometric object and provides methods for managing its properties.

    Attributes:
        _x (float): The x-coordinate of the geometric object.
        _y (float): The y-coordinate of the geometric object.
        color (str): The color of the geometric object.
        filled (bool): Whether the geometric object is filled or not.

    Methods:
        __init__: Initializes a GeometricObject object with specified coordinates, color, and filled status.
        set_coordinate: Sets the coordinates of the geometric object.
        set_color: Sets the color of the geometric object.
        set_filled: Sets the filled status of the geometric object.
        get_x: Returns the x-coordinate of the geometric object.
        get_y: Returns the y-coordinate of the geometric object.
        get_color: Returns the color of the geometric object.
        is_filled: Returns True if the geometric object is filled, False otherwise.
        __str__: Returns a string representation of the geometric object.
        __repr__: Returns a string representation of the geometric object.
    """
    def __init__(self, x=0.0, y=0.0, color='black', filled=False):
        """
         Initializes a GeometricObject object with specified coordinates, color, and filled status.

        Args:
            x (float): The x-coordinate of the geometric object. Defaults to 0.0.
            y (float): The y-coordinate of the geometric object. Defaults to 0.0.
            color (str): The color of the geometric object. Defaults to 'black'.
            filled (bool): Whether the geometric object is filled or not. Defaults to False.
        """
        self._x = float(x)
        self._y = float(y)
        self.color = color
        self.filled = filled

    def set_coordinate(self, new_x, new_y):
        """
        Sets the coordinates of the geometric object.

        Args:
            new_x (float): The new x-coordinate.
            new_y (float): The new y-coordinate.
        """
        self._x = float(new_x)
        self._y = float(new_y)

    def set_color(self, new_color):
        """
        Sets the color of the geometric object.

        Args:
            new_color (str): The new color.
        """
        self.color = new_color

    def set_filled(self, new_filled):
        """
        Sets the filled status of the geometric object.

        Args:
            new_filled (bool): The new filled status.
        """
        self.filled = new_filled

    def get_x(self):
        """
        Returns the x-coordinate of the geometric object.

        Returns:
            float: The x-coordinate.
        """
        return self._x

    def get_y(self):
        """
        Returns the y-coordinate of the geometric object.

        Returns:
            float: The y-coordinate.
        """
        return self._y

    def get_color(self):
        """
        Returns the color of the geometric object.

        Returns:
            str: The color.
        """
        return self.color

    def is_filled(self):
        """
        Returns True if the geometric object is filled, False otherwise.

        Returns:
            bool: True if the object is filled, False otherwise.
        """
        return self.filled

    def __str__(self):
        """
        Returns a string representation of the geometric object.

        Returns:
            str: The string representation.
        """
        return (f'({self._x},{self._y}) \n'
                f'color: {self.color} \n'
                f'filled: {self.filled}')

    def __repr__(self):
        """
        Returns a string representation of the geometric object.

        Returns:
            str: The string representation.
        """
        if self.filled:
            fil = 'filled'
        else:
            fil = 'no filled'
        return f'({int(self._x)},{int(self._y)}) {self.color} {fil}'


class Circle(GeometricObject):
    """
    Represents a circle and provides methods for managing its properties.

    Attributes:
        radius (float): The radius of the circle.

    Methods:
        __init__: Initializes a Circle object with specified coordinates, radius, color, and filled status.
        get_area: Calculates and returns the area of the circle.
        get_perimeter: Calculates and returns the perimeter of the circle.
        get_diameter: Calculates and returns the diameter of the circle.
        __str__: Returns a string representation of the circle.
        __repr__: Returns a string representation of the circle.
    """
    def __init__(self, x=0.0, y=0.0, radius=0.0, color='black', filled=False):
        """
        Initializes a Circle object with specified coordinates, radius, color, and filled status.

        Args:
            x (float): The x-coordinate of the center of the circle. Defaults to 0.0.
            y (float): The y-coordinate of the center of the circle. Defaults to 0.0.
            radius (float): The radius of the circle. Defaults to 0.0.
            color (str): The color of the circle. Defaults to 'black'.
            filled (bool): Whether the circle is filled or not. Defaults to False.
        """
        super().__init__(x, y, color, filled)
        if radius > 0:
            self.__radius = float(radius)
        else:
            self.__radius = 0.0

    @property
    def radius(self):
        """
        Getter method for the radius of the circle.

        Returns:
            float: The radius of the circle.
        """
        return self.__radius

    @radius.setter
    def radius(self, new_rad):
        """
        Setter method for the radius of the circle.

        Args:
            new_rad (float): The new value for the radius.
        """
        if new_rad > 0:
            self.__radius = float(new_rad)

    def get_area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def get_perimetr(self):
        """
        Calculates and returns the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.__radius

    def get_diametr(self):
        """
        Calculates and returns the diameter of the circle.

        Returns:
            float: The diameter of the circle.
        """
        return 2 * self.__radius

    def __str__(self):
        """
        Returns a string representation of the circle.

        Returns:
            str: The string representation.
        """
        return (f'radius: {self.__radius} \n'
                f'({self._x},{self._y}) \n'
                f'color: {self.color} \n'
                f'filled: {self.filled}')

    def __repr__(self):
        """
        Returns a string representation of the circle.

        Returns:
            str: The string representation.
        """
        if self.filled:
            fil = 'filled'
        else:
            fil = 'no filled'
        return f'radius: {int(self.radius)} ({int(self._x)},{int(self._y)}) {self.color} {fil}'


class Rectangle(GeometricObject):
    """
    Represents a rectangle and provides methods for managing its properties.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

    Methods:
        __init__: Initializes a Rectangle object with specified coordinates, width, height, color, and filled status.
        set_width: Sets the width of the rectangle.
        set_height: Sets the height of the rectangle.
        get_width: Returns the width of the rectangle.
        get_height: Returns the height of the rectangle.
        get_area: Calculates and returns the area of the rectangle.
        get_perimeter: Calculates and returns the perimeter of the rectangle.
        __str__: Returns a string representation of the rectangle.
        __repr__: Returns a string representation of the rectangle.
    """
    def __init__(self, x=0.0, y=0.0, width=0.0, height=0.0, color='black', filled=False):
        """
        Initializes a Rectangle object with specified coordinates, width, height, color, and filled status.

        Args:
            x (float): The x-coordinate of the top-left corner of the rectangle. Defaults to 0.0.
            y (float): The y-coordinate of the top-left corner of the rectangle. Defaults to 0.0.
            width (float): The width of the rectangle. Defaults to 0.0.
            height (float): The height of the rectangle. Defaults to 0.0.
            color (str): The color of the rectangle. Defaults to 'black'.
            filled (bool): Whether the rectangle is filled or not. Defaults to False.
        """
        super().__init__(x, y, color, filled)
        if width > 0:
            self.width = float(width)
        else:
            self.width = 0.0
        if height > 0:
            self.height = float(height)
        else:
            self.height = 0.0

    def set_width(self, new_width):
        """
        Sets the width of the rectangle.

        Args:
            new_width (float): The new width of the rectangle.
        """
        if new_width > 0:
            self.width = float(new_width)

    def set_height(self, new_height):
        """
        Sets the height of the rectangle.

        Args:
            new_height (float): The new height of the rectangle.
        """
        if new_height > 0:
            self.height = float(new_height)

    def get_width(self):
        """
        Returns the width of the rectangle.

        Returns:
            float: The width of the rectangle.
        """
        return self.width

    def get_height(self):
        """
        Returns the height of the rectangle.

        Returns:
            float: The height of the rectangle.
        """
        return self.height

    def get_area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.height * self.width

    def get_perimetr(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.height + self.width)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return (f'width: {self.width} \n'
                f'height: {self.height} \n'
                f'({self._x},{self._y}) \n'
                f'color: {self.color} \n'
                f'filled: {self.filled}')

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        if self.filled:
            fil = 'filled'
        else:
            fil = 'no filled'
        return f'width: {int(self.width)} height: {int(self.height)} ({int(self._x)},{int(self._y)}) {self.color} {fil}'
