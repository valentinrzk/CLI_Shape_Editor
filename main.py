"""
Точка входа CLI редактора.
"""

from editor.shape_storage import ShapeStorage
from editor.command_registry import COMMAND_REGISTRY

import shape.shapes
import editor.commands


def main():

    storage = ShapeStorage()

    print("CLI Векторный редактор")
    print("Введите help для списка команд")

    while True:

        command = input(">>> ").strip()

        if not command:
            continue

        if command == "exit":
            break

        parts = command.split()

        name = parts[0]
        args = parts[1:]

        try:

            if name not in COMMAND_REGISTRY:
                print(f"Неизвестная команда: {name}")
                continue

            cmd = COMMAND_REGISTRY[name](storage)
            print(cmd.execute(args))

        except Exception as e:
            print("Ошибка:", e)


if __name__ == "__main__":
    main()