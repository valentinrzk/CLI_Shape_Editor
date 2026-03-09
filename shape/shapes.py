"""
Реализации фигур.
"""

import math
from shape.shape_base import Shape
from shape.shape_registry import register_shape


@register_shape("point")
class Point(Shape):
    """
    Геометрическая точка.
    """

    def __init__(self, shape_id: int, x: float, y: float):
        super().__init__(shape_id)
        self.x = x
        self.y = y

    def info(self) -> str:
        return f"Point(id={self.id}, x={self.x}, y={self.y})"

    def area(self) -> float:
        return 0.0

    def perimeter(self) -> float:
        return 0.0


@register_shape("line")
class Line(Shape):
    """
    Геометрический отрезок, заданный двумя точками.
    """

    def __init__(self, shape_id: int, x1: float, y1: float, x2: float, y2: float):
        """
        Создание отрезка.

        :param shape_id: уникальный идентификатор фигуры
        :param x1: координата X первой точки
        :param y1: координата Y первой точки
        :param x2: координата X второй точки
        :param y2: координата Y второй точки
        """

        super().__init__(shape_id)

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def info(self) -> str:
        """
        Вернуть текстовое описание отрезка.
        """

        return f"Line(id={self.id}, ({self.x1},{self.y1}) -> ({self.x2},{self.y2}))"

    def area(self) -> float:
        """
        Площадь отрезка равна нулю.
        """

        return 0.0

    def perimeter(self) -> float:
        """
        Периметр отрезка равен его длине.
        """

        dx = self.x2 - self.x1
        dy = self.y2 - self.y1

        return math.sqrt(dx ** 2 + dy ** 2)


@register_shape("circle")
class Circle(Shape):

    def __init__(self, shape_id: int, x: float, y: float, r: float):
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.r = r

    def info(self) -> str:
        return f"Circle(id={self.id}, center=({self.x},{self.y}), r={self.r})"

    def area(self) -> float:
        return math.pi * self.r ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.r


@register_shape("square")
class Square(Shape):
    """
    Квадрат.
    """

    def __init__(self, shape_id: int, x: float, y: float, side: float):
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.side = side

    def info(self) -> str:
        return f"Square(id={self.id}, corner=({self.x},{self.y}), side={self.side})"

    def area(self) -> float:
        return self.side ** 2

    def perimeter(self) -> float:
        return 4 * self.side

@register_shape("rectangle")
class Rectangle(Shape):
    """
    Прямоугольник.
    """

    def __init__(self, shape_id: int, x: float, y: float, width: float, height: float):
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def info(self) -> str:
        return f"Rectangle(id={self.id}, corner=({self.x},{self.y}), width={self.width}, height={self.height})"

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)