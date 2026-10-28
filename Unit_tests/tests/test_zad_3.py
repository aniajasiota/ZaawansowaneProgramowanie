from zad_3 import count_vowels

def test_count_vowels():
    assert count_vowels('Python') == 2

def test_count_vowels_2():
    assert count_vowels('AEIOUY') == 6

def test_count_vowels_3():
    assert count_vowels('bcd') == 0

def test_count_vowels_4():
    assert count_vowels('') == 0

def test_count_vowels_5():
    assert count_vowels('Próba żółwia') == 5