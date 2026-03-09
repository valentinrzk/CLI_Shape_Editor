"""
Хранилище фигур.
"""

from typing import Dict, List
from shape.shape_base import Shape


class ShapeStorage:

    def __init__(self):
        self._shapes: Dict[int, Shape] = {}
        self._next_id = 1

    def generate_id(self) -> int:
        shape_id = self._next_id
        self._next_id += 1
        return shape_id

    def add(self, shape: Shape):
        self._shapes[shape.id] = shape

    def remove(self, shape_id: int):
        self._shapes.pop(shape_id, None)

    def get(self, shape_id: int) -> Shape:
        return self._shapes[shape_id]

    def list(self) -> List[Shape]:
        return list(self._shapes.values())