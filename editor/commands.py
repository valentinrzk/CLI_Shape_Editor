"""
Реализации CLI команд.
"""

from editor.command_base import Command
from editor.command_registry import register_command, COMMAND_REGISTRY
from shape.shape_registry import SHAPE_REGISTRY
from editor.shape_factory import ShapeFactory
from editor.file_service import ShapeFileService


@register_command("help")
class HelpCommand(Command):
    """
    Показать список доступных команд.
    Информация о командах берется из их docstring, а также из атрибута syntax для команд создания фигур.
    """

    def execute(self, args: list[str]) -> str:
        """
        Вывести список команд и их описание.
        """
        lines = ["Доступные команды:\n"]

        for name, cmd_class in COMMAND_REGISTRY.items():
            description = cmd_class.__doc__ or ""
            description = description.strip()
            lines.append(f"{name:<10} - {description}")

        lines.append("\nСинтаксис создания фигур:\n")

        for shape_name, shape_class in SHAPE_REGISTRY.items():
            if hasattr(shape_class, 'syntax'):
                syntax = shape_class.syntax
                lines.append(f"{syntax.command:<30} {syntax.description}")

        return "\n".join(lines)


@register_command("add")
class AddCommand(Command):
    """
    Создать фигуру. Подробности создания фигур см. в разделе "Синтаксис создания фигур"
    """

    def execute(self, args: list[str]) -> str:

        if not args:
            raise ValueError("Не указан тип фигуры")

        shape_type = args[0]
        shape_args = args[1:]

        shape = ShapeFactory.create(
            shape_type,
            self.storage.generate_id(),
            shape_args
        )

        self.storage.add(shape)

        return f"Создана фигура: {shape.info()}"

@register_command("list")
class ListCommand(Command):
    """
    Команда вывода списка фигур.
    """

    def execute(self, args: list[str]) -> str:

        shapes = self.storage.list()

        if not shapes:
            return "Список фигур пуст"

        return "\n".join(s.info() for s in shapes)

@register_command("delete")
class DeleteCommand(Command):
    """
    Команда удаления фигуры.
    """

    def execute(self, args: list[str]) -> str:

        shape_id = int(args[0])
        self.storage.remove(shape_id)

        return f"Фигура {shape_id} удалена"

@register_command("area")
class AreaCommand(Command):
    """
    Команда вычисления площади фигуры.
    """

    def execute(self, args: list[str]) -> str:

        shape_id = int(args[0])
        shape = self.storage.get(shape_id)

        return f"Площадь: {shape.area()}"

@register_command("perimeter")
class PerimeterCommand(Command):
    """
    Команда вычисления периметра фигуры.
    """

    def execute(self, args: list[str]) -> str:

        shape_id = int(args[0])
        shape = self.storage.get(shape_id)

        return f"Периметр: {shape.perimeter()}"

@register_command("clear")
class ClearCommand(Command):
    """
    Команда очистки всех фигур.
    """

    def execute(self, args: list[str]) -> str:

        self.storage.clear()

        return "Все фигуры удалены"

@register_command("save")
class SaveCommand(Command):
    """
    Сохранить фигуры в файл.
    """

    def execute(self, args: list[str]) -> str:

        if not args:
            raise ValueError("Не указано имя файла")

        path = args[0]

        if not path.endswith(".json"):
            path += ".json"

        ShapeFileService.save(self.storage, path)

        return f"Фигуры сохранены в {path}"

@register_command("load")
class LoadCommand(Command):
    """
    Загрузить фигуры из файла.
    """

    def execute(self, args: list[str]) -> str:

        if not args:
            raise ValueError("Не указано имя файла")

        path = args[0]

        if not path.endswith(".json"):
            path += ".json"

        ShapeFileService.load(self.storage, path)

        return f"Фигуры загружены из {path}"