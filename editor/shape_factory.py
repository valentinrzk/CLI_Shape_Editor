"""
Фабрика создания фигур.

Использует реестр фигур (SHAPE_REGISTRY) для динамического
создания объектов нужного типа.
"""

from shape.shape_registry import SHAPE_REGISTRY
from shape.shape_base import Shape


class ShapeFactory:
    """
    Фабрика для создания фигур по имени типа.
    """

    @staticmethod
    def create(shape_type: str, shape_id: int, args: list[str]) -> Shape:
        """
        Создать фигуру указанного типа.

        :param shape_type: имя фигуры (point, line, circle, square)
        :param shape_id: уникальный идентификатор фигуры
        :param args: аргументы из CLI
        :return: объект фигуры
        """

        if shape_type not in SHAPE_REGISTRY:
            raise ValueError(f"Неизвестный тип фигуры: {shape_type}")

        shape_class = SHAPE_REGISTRY[shape_type]

        numeric_args = list(map(float, args))

        return shape_class(*numeric_args, id=shape_id)

    @staticmethod
    def create_from_dict(data: dict):
        """
        Создать фигуру из словаря данных (например, при загрузке из файла).
        :param data: Словарь с данными фигуры, должен содержать ключ "type" для определения типа фигуры.
        :return:
        """
        shape_type = data.pop("type")

        shape_class = SHAPE_REGISTRY.get(shape_type)

        if not shape_class:
            raise ValueError(f"Неизвестный тип фигуры: {shape_type}")

        return shape_class(**data)