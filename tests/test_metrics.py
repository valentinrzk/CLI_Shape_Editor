from editor.commands import AreaCommand
from editor.commands import PerimeterCommand
from editor.commands import AddCommand


def test_area_circle(storage):

    AddCommand(storage).execute(["circle", "0", "0", "10"])

    result = AreaCommand(storage).execute(["1"])

    assert "Площадь:" in result
    value = float(result.split(":")[1].strip())
    assert value > 0

def test_perimeter_square(storage):

    AddCommand(storage).execute(["square", "0", "0", "10"])

    result = PerimeterCommand(storage).execute(["1"])

    assert "Периметр:" in result
    value = float(result.split(":")[1].strip())
    assert value > 0

