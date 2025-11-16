import pytest
from testy_jednostkowe_log import is_palindrome
from testy_jednostkowe_log import fibonacci
from testy_jednostkowe_log import count_vowels
from testy_jednostkowe_log import calculate_discount

@pytest.mark.parametrize("text, expected", [
    ("kajak", True),
    ("Kobyła ma mały bok", True),
    ("python", False),
    ("", True),
    ("A", True),
])
def test_is_palindrome(text, expected):
    assert is_palindrome(text) == expected

@pytest.mark.parametrize('n, expected',  [
    (0, 0),
    (1, 1),
    (5,5),
    (10, 55),
    (-1, ValueError)
])
def test_fibonacci(n, expected):
    if expected is ValueError:
        with pytest.raises(ValueError):
            fibonacci(n)
    else:
        assert fibonacci(n) == expected


@pytest.mark.parametrize('tekst, expected', [
    ('Python', 2),
    ('AEIOUY', 6),
    ('bcd',0),
    ("",0),
    ('Próba żółwia', 5)
])

def test_count_vowels(tekst, expected):
    assert count_vowels(tekst) == expected


@pytest.mark.parametrize('price, discount, expected', [
    (100,0.2,80),
    (50,0,50.0),
    (200,1,0.0),
    (100,-0.1,ValueError),
    (100,1.5,ValueError)
])
def test_calculate_discount(price,discount, expected):
    if expected is ValueError:
        with pytest.raises(ValueError):
            calculate_discount(price,discount)
    else:
        assert calculate_discount(price,discount) == expected