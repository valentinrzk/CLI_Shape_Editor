"""
Реализации конкретных видов фигур с добавление в реестр.
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
        """
        Создание точки.
        :param shape_id: Идентификатор фигуры
        :param x: Координата X
        :param y: Координата Y
        """
        super().__init__(shape_id)
        self.x = x
        self.y = y

    def to_dict(self) -> dict:
        return {
            "type": "point",
            "id": self.id,
            "x": self.x,
            "y": self.y
        }

    def info(self) -> str:
        return f"Point(id={self.id}, x={self.x}, y={self.y})"

    def area(self) -> float:
        """Возвращает площадь фигуры. Для точки это всегда 0."""
        return 0.0

    def perimeter(self) -> float:
        """Возвращает периметр фигуры. Для точки это всегда 0."""
        return 0.0


@register_shape("line")
class Line(Shape):
    """
    Геометрическая линия, отрезок, заданный двумя точками.
    """

    def __init__(self, shape_id: int, x1: float, y1: float, x2: float, y2: float):
        """
        Создание отрезка.

        :param shape_id: Идентификатор фигуры
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
        Возвращает площадь фигуры. Для линии это всегда 0.
        """

        return 0.0

    def perimeter(self) -> float:
        """
        Возвращает периметр фигуры. Для линии это длина отрезка, вычисляемая по формуле расстояния между двумя точками.
        """

        dx = self.x2 - self.x1
        dy = self.y2 - self.y1

        return math.sqrt(dx ** 2 + dy ** 2)

    def to_dict(self) -> dict:
        return {
            "type": "line",
            "id": self.id,
            "x1": self.x1,
            "y1": self.y1,
            "x2": self.x2,
            "y2": self.y2
        }


@register_shape("circle")
class Circle(Shape):
    """
    Окружность. Задается центром и радиусом.
    """

    def __init__(self, shape_id: int, x: float, y: float, r: float):
        """
        Создание окружности.
        :param shape_id: Идентификатор фигуры
        :param x: Координата X центра
        :param y: Координата Y центра
        :param r: Радиус окружности
        """
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.r = r

    def info(self) -> str:
        return f"Circle(id={self.id}, center=({self.x},{self.y}), r={self.r})"

    def area(self) -> float:
        """
        Возвращает площадь фигуры. Для окружности это π * r^2.
        """
        return math.pi * self.r ** 2

    def perimeter(self) -> float:
        """
        Возвращает периметр фигуры. Для окружности это 2 * π * r.
        """
        return 2 * math.pi * self.r

    def to_dict(self) -> dict:
        return {
            "type": "circle",
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "r": self.r
        }


@register_shape("square")
class Square(Shape):
    """
    Квадрат. Задан координатами левого верхнего угла и длиной стороны.
    """

    def __init__(self, shape_id: int, x: float, y: float, side: float):
        """
        Создание квадрата.
        :param shape_id: Идентификатор фигуры
        :param x: Координата X левого верхнего угла
        :param y:  Координата Y левого верхнего угла
        :param side: Длина стороны квадрата
        """
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.side = side

    def info(self) -> str:
        return f"Square(id={self.id}, corner=({self.x},{self.y}), side={self.side})"

    def area(self) -> float:
        """
        Возвращает площадь фигуры. Для квадрата это side^2.
        """
        return self.side ** 2

    def perimeter(self) -> float:
        """
        Возвращает периметр фигуры. Для квадрата это 4 * side.
        """
        return 4 * self.side

    def to_dict(self) -> dict:
        return {
            "type": "square",
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "side": self.side
        }

@register_shape("rectangle")
class Rectangle(Shape):
    """
    Прямоугольник. Задан координатами левого верхнего угла, шириной и высотой.
    """

    def __init__(self, shape_id: int, x: float, y: float, width: float, height: float):
        """
        Создание прямоугольника.
        :param shape_id: Идентификатор фигуры
        :param x: Координата X левого верхнего угла
        :param y: Координата Y левого верхнего угла
        :param width: Ширина прямоугольника
        :param height: Высота прямоугольника
        """
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def info(self) -> str:
        return f"Rectangle(id={self.id}, corner=({self.x},{self.y}), width={self.width}, height={self.height})"

    def area(self) -> float:
        """
        Возвращает площадь фигуры. Для прямоугольника это width * height.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Возвращает периметр фигуры. Для прямоугольника это 2 * (width + height).
        """
        return 2 * (self.width + self.height)

    def to_dict(self) -> dict:
        return {
            "type": "rectangle",
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "width": self.width,
            "height": self.height
        }

@register_shape("ellipse")
class Ellipse(Shape):
    """
    Овал (эллипс). Задан координатами центра и радиусами по осям X и Y.
    """

    def __init__(self, shape_id: int, x: float, y: float, xr: float, yr: float):
        """
        Создание эллипса.
        :param shape_id: Идентификатор фигуры
        :param x: Координата X центра
        :param y: Координата Y центра
        :param xr: Радиус по оси X
        :param yr: Радиус по оси Y
        """
        super().__init__(shape_id)
        self.x = x
        self.y = y
        self.xr = xr
        self.yr = yr

    def info(self) -> str:
        return f"Ellipse(id={self.id}, center=({self.x},{self.y}), x_radius={self.xr}, y_radius={self.yr})"

    def area(self) -> float:
        """
        Возвращает площадь фигуры. Для эллипса это π * xr * yr.
        """
        return math.pi * self.xr * self.yr

    def perimeter(self) -> float:
        """
        Возвращает периметр фигуры. Для эллипса в данном примере используем приближенную формулу Раманауджана.
        """
        h = ((self.xr - self.yr) ** 2) / ((self.xr + self.yr) ** 2)
        return math.pi * (self.xr + self.yr) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))

    def to_dict(self) -> dict:
        return {
            "type": "ellipse",
            "id": self.id,
            "x": self.x,
            "y": self.y,
            "xr": self.xr,
            "yr": self.yr
        }