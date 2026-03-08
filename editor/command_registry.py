"""
Реестр CLI команд.
"""

from typing import Type
from editor.command_base import Command


COMMAND_REGISTRY: dict[str, Type[Command]] = {}


def register_command(name: str):
    """
    Декоратор для регистрации команды.
    """

    def decorator(cls: Type[Command]):
        COMMAND_REGISTRY[name] = cls
        return cls

    return decorator