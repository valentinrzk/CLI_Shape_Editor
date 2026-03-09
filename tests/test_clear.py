import pytest
from editor.commands import ClearCommand, AddCommand, ListCommand


def test_clear_empty_storage(storage):
    """
    Тест проверяет, что clear работает на пустом хранилище.
    """
    cmd = ClearCommand(storage)
    result = cmd.execute([])

    assert "удалены" in result.lower()
    assert len(storage.list()) == 0


def test_clear_with_shapes(storage):
    """
    Тест проверяет, что clear удаляет все фигуры из хранилища.
    """
    AddCommand(storage).execute(["point", "0", "0"])
    AddCommand(storage).execute(["circle", "1", "1", "5"])
    AddCommand(storage).execute(["square", "2", "2", "10"])

    assert len(storage.list()) == 3

    result = ClearCommand(storage).execute([])

    assert "удалены" in result.lower()
    assert len(storage.list()) == 0


def test_clear_ignores_args(storage):
    """
    Тест проверяет, что clear игнорирует переданные аргументы.
    """
    AddCommand(storage).execute(["point", "0", "0"])

    result = ClearCommand(storage).execute(["some", "args"])

    assert len(storage.list()) == 0
