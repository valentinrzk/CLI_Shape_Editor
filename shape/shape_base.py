"""
Базовые определения геометрических фигур.

В этом модуле объявляется абстрактный класс Shape, от которого
наследуются все фигуры редактора.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """
    Абстрактный базовый класс геометрической фигуры.

    Каждая фигура имеет уникальный идентификатор,
    который назначается хранилищем фигур.
    """

    def __init__(self, id: int):
        """
        Создание фигуры.

        :param id: Уникальный идентификатор фигуры
        """
        self.id = id

    @abstractmethod
    def info(self) -> str:
        """
        Вернуть текстовое описание фигуры.
        """
        pass

    @abstractmethod
    def area(self) -> float:
        """
        Вернуть площадь фигуры.
        """
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """
        Вернуть периметр фигуры.
        """
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        """
        Вернуть словарь с данными фигуры для сохранения в JSON.
        """
        pass