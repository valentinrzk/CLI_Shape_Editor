"""
Хранилище фигур.
"""

from typing import Dict, List
from shape.shape_base import Shape


class ShapeStorage:
    """
    Класс для хранения фигур.
    """

    def __init__(self):
        """
        Инициализация хранилища.
        """
        self._shapes: Dict[int, Shape] = {}
        self._next_id = 1

    def exists(self, shape_id: int) -> bool:
        """
        Проверить, существует ли фигура с данным id.
        """
        return shape_id in self._shapes

    def generate_id(self) -> int:
        """
        Сгенерировать новый уникальный идентификатор для фигуры.
        :return: Новый уникальный идентификатор
        """
        shape_id = self._next_id
        self._next_id += 1
        return shape_id

    def add(self, shape: Shape):
        """
        Добавить фигуру в хранилище.
        :param shape: Фигура для добавления
        :return:
        """
        self._shapes[shape.id] = shape

    def remove(self, shape_id: int):
        """
        Удалить фигуру из хранилища по id.
        :param shape_id: Идентификатор фигуры для удаления
        :return:
        """
        self._shapes.pop(shape_id, None)

    def get(self, shape_id: int) -> Shape:
        """
        Получить фигуру по id.
        :param shape_id: Идентификатор фигуры для получения
        :return:
        """
        if shape_id not in self._shapes:
            raise ValueError(f"Фигура с id {shape_id} не найдена")
        return self._shapes[shape_id]

    def list(self) -> List[Shape]:
        """
        Получить список всех фигур в хранилище.
        :return: Список фигур
        """
        return list(self._shapes.values())

    def clear(self):
        """
        Очистить хранилище фигур.
        """
        self._shapes.clear()

    def sync_next_id(self):
        """
        Синхронизирует счетчик id после загрузки фигур.
        """
        if not self._shapes:
            self._next_id = 1
        else:
            self._next_id = max(self._shapes.keys()) + 1