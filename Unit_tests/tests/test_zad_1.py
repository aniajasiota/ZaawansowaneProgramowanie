from zad_1 import ispalindrome

def test_ispalindrome():
    assert ispalindrome("kajak") is True

def test_ispalindrome2():
    assert ispalindrome("Kobyła ma mały bok") is True

def test_ispalindrome3():
    assert ispalindrome("python") is False

def test_ispalindrome4():
    assert ispalindrome("") is True

def test_ispalindrome5():
    assert ispalindrome("A") is True