import pytest

import shape.shapes
import editor.commands
from editor.storage import ShapeStorage


@pytest.fixture
def storage():
    return ShapeStorage()