from editor.commands import ListCommand
from editor.commands import AddCommand


def test_list_empty(storage):

    cmd = ListCommand(storage)

    result = cmd.execute([])

    assert result == "Список фигур пуст"


def test_list_with_shapes(storage):

    AddCommand(storage).execute(["point", "0", "0"])

    result = ListCommand(storage).execute([])

    assert "Point" in result

