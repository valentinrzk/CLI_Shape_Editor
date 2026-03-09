import pytest
import json
from pathlib import Path
from editor.commands import LoadCommand, SaveCommand, AddCommand, ListCommand


def test_load_basic(storage, tmp_path, monkeypatch):
    """
    Тест проверяет базовую загрузку фигур из файла.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    AddCommand(storage).execute(["point", "0", "0"])
    AddCommand(storage).execute(["circle", "1", "1", "5"])
    SaveCommand(storage).execute(["shapes"])

    storage.clear()
    assert len(storage.list()) == 0

    result = LoadCommand(storage).execute(["shapes"])

    assert "загружены" in result.lower()
    assert len(storage.list()) == 2


def test_load_with_json_extension(storage, tmp_path, monkeypatch):
    """
    Тест проверяет, что расширение .json добавляется автоматически при загрузке.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    AddCommand(storage).execute(["point", "3", "4"])
    SaveCommand(storage).execute(["test_data.json"])

    storage.clear()

    result = LoadCommand(storage).execute(["test_data"])

    assert "загружены" in result.lower()
    assert len(storage.list()) == 1


def test_load_empty_file(storage, tmp_path, monkeypatch):
    """
    Тест проверяет загрузку пустого файла.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    SaveCommand(storage).execute(["empty"])

    storage.clear()

    result = LoadCommand(storage).execute(["empty"])

    assert "загружены" in result.lower()
    assert len(storage.list()) == 0


def test_load_without_filename(storage):
    """
    Тест проверяет, что ошибка выбрасывается при отсутствии имени файла.
    """
    with pytest.raises(ValueError):
        LoadCommand(storage).execute([])


def test_load_nonexistent_file(storage, tmp_path, monkeypatch):
    """
    Тест проверяет ошибку при загрузке несуществующего файла.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    with pytest.raises(FileNotFoundError):
        LoadCommand(storage).execute(["nonexistent"])


def test_load_preserves_shape_data(storage, tmp_path, monkeypatch):
    """
    Тест проверяет, что данные фигур сохраняются правильно при загрузке.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    AddCommand(storage).execute(["circle", "5", "10", "15"])
    SaveCommand(storage).execute(["circles"])

    storage.clear()
    LoadCommand(storage).execute(["circles"])

    shapes = storage.list()
    assert len(shapes) == 1
    assert shapes[0].__class__.__name__ == "Circle"
    assert shapes[0].x == 5
    assert shapes[0].y == 10
    assert shapes[0].r == 15


def test_load_syncs_next_id(storage, tmp_path, monkeypatch):
    """
    Тест проверяет, что счетчик id синхронизируется правильно после загрузки.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    AddCommand(storage).execute(["point", "0", "0"])
    AddCommand(storage).execute(["point", "1", "1"])
    SaveCommand(storage).execute(["ids_test"])

    storage.clear()
    LoadCommand(storage).execute(["ids_test"])

    result = AddCommand(storage).execute(["point", "2", "2"])

    assert "id=3" in result


def test_load_clears_previous_shapes(storage, tmp_path, monkeypatch):
    """
    Тест проверяет, что load очищает предыдущие фигуры перед загрузкой.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    AddCommand(storage).execute(["point", "0", "0"])
    SaveCommand(storage).execute(["file1"])

    AddCommand(storage).execute(["circle", "1", "1", "5"])
    SaveCommand(storage).execute(["file2"])

    LoadCommand(storage).execute(["file1"])

    assert len(storage.list()) == 1
    assert storage.list()[0].__class__.__name__ == "Point"
