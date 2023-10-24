import pytest

from engine.engine2d import Engine2D


@pytest.fixture(scope='function')
def engine_object():
    return Engine2D(800, 600, "2D-движок")