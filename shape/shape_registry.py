"""
Реестр доступных типов фигур.

Позволяет регистрировать фигуры через декоратор
и использовать их в фабрике без изменения кода фабрики.
"""

from typing import Type
from shape.shape_base import Shape


SHAPE_REGISTRY: dict[str, Type[Shape]] = {}


def register_shape(name: str):
    """
    Декоратор для регистрации новой фигуры.

    :param name: имя фигуры в CLI
    """

    def decorator(cls: Type[Shape]):
        SHAPE_REGISTRY[name] = cls
        return cls

    return decorator