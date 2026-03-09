import pytest
from editor.commands import AddCommand


@pytest.mark.parametrize(
    "shape_name,args,expected_class",
    [
        ("point", ["0", "0"], "Point"),
        ("line", ["0", "0", "1", "1"], "Line"),
        ("circle", ["0", "0", "5"], "Circle"),
        ("square", ["0", "0", "10"], "Square"),
        ("rectangle", ["0", "0", "10", "5"], "Rectangle"),
        ("ellipse", ["0", "0", "10", "5"], "Ellipse"),
    ]
)
def test_add_shapes_positive(storage, shape_name, args, expected_class):
    """
    Позитивные тесты команды add для разных типов фигур.
    """
    cmd = AddCommand(storage)
    result = cmd.execute([shape_name] + args)

    assert expected_class in result

    shapes = storage.list()
    assert len(shapes) == 1
    assert shapes[0].__class__.__name__ == expected_class

def test_add_without_args(storage):

    cmd = AddCommand(storage)

    with pytest.raises(ValueError):
        cmd.execute([])

def test_add_unknown_shape(storage):

    cmd = AddCommand(storage)

    with pytest.raises(ValueError):
        cmd.execute(["triangle", "0", "0"])


def test_add_point_extra_argument(storage):

    cmd = AddCommand(storage)

    with pytest.raises(TypeError):
        cmd.execute(["point", "1", "1", "1"])

