from editor.commands import HelpCommand


def test_help_basic(storage):

    cmd = HelpCommand(storage)

    result = cmd.execute([])

    assert "point" in result
    assert "line" in result
    assert "circle" in result
    assert "square" in result


def test_help_with_args(storage):

    cmd = HelpCommand(storage)

    result = cmd.execute(["anything"])

    assert "point" in result