import json
from pathlib import Path
from editor.shape_factory import ShapeFactory


DATA_DIR = Path("data")

class ShapeFileService:
    """
    Сервис для сохранения и загрузки фигур из JSON-файла.
    """

    @staticmethod
    def _build_path(filename: str) -> Path:
        """
        Построить полный путь к файлу в папке data.
        Если имя файла не заканчивается на .json, добавить расширение.
        Если папки data нет, создать её.
        """

        if not filename.endswith(".json"):
            filename += ".json"

        DATA_DIR.mkdir(exist_ok=True)

        return DATA_DIR / filename

    @staticmethod
    def save(storage, filename: str) -> None:
        """
        Сохраняет фигуры из хранилища в JSON файл.
        :param storage: Хранилище фигур
        :param filename: Имя файла для сохранения (без расширения)
        :return:
        """
        path = ShapeFileService._build_path(filename)

        shapes = storage.list()
        data = [shape.to_dict() for shape in shapes]

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load(storage, filename: str) -> None:
        """
        Загружает фигуры из JSON файла в хранилище.
        :param storage: Хранилище фигур
        :param filename: Имя файла для загрузки (без расширения)
        :return:
        """
        path = ShapeFileService._build_path(filename)

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        storage.clear()

        for item in data:
            shape = ShapeFactory.create_from_dict(item)
            storage.add(shape)