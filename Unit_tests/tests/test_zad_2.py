import pytest
from zad_2 import fibonacci

def test_fibonacci():
    assert fibonacci(0) == 0

def test_fibonacci2():
    assert fibonacci(1) == 1

def test_fibonacci3():
    assert fibonacci(5) == 5

def test_fibonacci4():
    assert fibonacci(10) == 55

def test_fibonacci5():
    with pytest.raises(ValueError):
        fibonacci(-1)