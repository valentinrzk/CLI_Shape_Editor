from editor.commands import DeleteCommand
from editor.commands import AddCommand


def test_delete_existing(storage):

    AddCommand(storage).execute(["point", "0", "0"])

    DeleteCommand(storage).execute(["1"])

    assert len(storage.list()) == 0

def test_delete_nonexistent(storage):

    AddCommand(storage).execute(["point", "0", "0"])

    DeleteCommand(storage).execute(["999"])

    assert len(storage.list()) == 1


