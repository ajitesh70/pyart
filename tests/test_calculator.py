import pytest
from calculator import add, subtract, divide


def test_add_integers():
    assert add(2, 3) == 5


def test_add_negatives():
    assert add(-1, -1) == -2


def test_subtract():
    assert subtract(5, 2) == 3


def test_divide():
    assert divide(10, 2) == 5


def test_divide_float():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
