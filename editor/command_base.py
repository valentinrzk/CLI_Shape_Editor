"""
Базовый класс команды.

Все команды CLI наследуются от этого класса.
"""

from abc import ABC, abstractmethod
from editor.storage import ShapeStorage


class Command(ABC):
    """
    Абстрактная команда CLI.
    """

    description: str = ""

    def __init__(self, storage: ShapeStorage):
        self.storage = storage

    @abstractmethod
    def execute(self, args: list[str]) -> str:
        """
        Выполнить команду.
        """
        pass