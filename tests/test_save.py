import pytest
import json
from pathlib import Path
from editor.commands import SaveCommand, AddCommand


def test_save_basic(storage, tmp_path, monkeypatch):
    """
    Тест проверяет базовое сохранение фигур в файл.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    AddCommand(storage).execute(["point", "0", "0"])
    AddCommand(storage).execute(["circle", "1", "1", "5"])

    result = SaveCommand(storage).execute(["shapes"])

    assert "сохранены" in result.lower()

    saved_file = tmp_path / "shapes.json"
    assert saved_file.exists()

    with open(saved_file, "r") as f:
        data = json.load(f)

    assert len(data) == 2
    assert data[0]["type"] == "point"
    assert data[1]["type"] == "circle"


def test_save_with_json_extension(storage, tmp_path, monkeypatch):
    """
    Тест проверяет, что расширение .json добавляется автоматически.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    AddCommand(storage).execute(["point", "5", "5"])

    result = SaveCommand(storage).execute(["data.json"])

    assert "сохранены" in result.lower()
    assert (tmp_path / "data.json").exists()


def test_save_empty_storage(storage, tmp_path, monkeypatch):
    """
    Тест проверяет сохранение пустого хранилища.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    result = SaveCommand(storage).execute(["empty"])

    assert "сохранены" in result.lower()

    saved_file = tmp_path / "empty.json"
    with open(saved_file, "r") as f:
        data = json.load(f)

    assert len(data) == 0


def test_save_without_filename(storage):
    """
    Тест проверяет, что ошибка выбрасывается при отсутствии имени файла.
    """
    with pytest.raises(ValueError):
        SaveCommand(storage).execute([])


def test_save_overwrites_existing_file(storage, tmp_path, monkeypatch):
    """
    Тест проверяет, что сохранение перезаписывает существующий файл.
    """
    monkeypatch.setattr("editor.file_service.DATA_DIR", tmp_path)

    AddCommand(storage).execute(["point", "0", "0"])
    SaveCommand(storage).execute(["test"])

    storage.clear()
    AddCommand(storage).execute(["circle", "1", "1", "10"])
    SaveCommand(storage).execute(["test"])

    saved_file = tmp_path / "test.json"
    with open(saved_file, "r") as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]["type"] == "circle"
