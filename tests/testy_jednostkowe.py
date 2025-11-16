import pytest
from testy_jednostkowe_log import is_palindrome
from testy_jednostkowe_log import fibonacci

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