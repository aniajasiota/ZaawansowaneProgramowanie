from zad_7 import is_prime

def test_is_prime():
    assert is_prime(2) is True

def test_is_prime_2():
    assert is_prime(3) is True

def test_is_prime_3():
    assert is_prime(4) is False

def test_is_prime_4():
    assert is_prime(0) is False

def test_is_prime_5():
    assert is_prime(1) is False

def test_is_prime_6():
    assert is_prime(5) is True

def test_is_prime_7():
    assert is_prime(97) is True