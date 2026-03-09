import pytest

import shape.shapes
import editor.commands
from editor.shape_storage import ShapeStorage


@pytest.fixture
def storage():
    return ShapeStorage()