import pytest
from zad_4 import calculate_discount

def test_discount():
    assert calculate_discount(100, 0.2) == 80

def test_discount_2():
    assert calculate_discount(50, 0) == 50

def test_discount_3():
    assert calculate_discount(200, 1) == 0.0

def test_discount_4():
    with pytest.raises(ValueError):
        calculate_discount(100, -0.1)

def test_discount_5():
    with pytest.raises(ValueError):
        calculate_discount(100, 1.5)