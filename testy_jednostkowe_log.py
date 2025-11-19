def is_palindrome(tekst: str) -> bool:
    cleaned = tekst.replace(" ", "").lower()
    return cleaned == cleaned[::-1]


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError
    if n in (0, 1):
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def count_vowels(tekst: str) -> int:
    vowels = 'aeiouyąęó'
    return sum(1 for char in tekst.lower() if char in vowels)


def calculate_discount(price: float, discount: float) -> float:
    if discount < 0 or discount > 1:
        raise ValueError
    else:
        return price - (price * discount)


def flatten_list(nested_list: list) -> list:
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def word_frequencies(text: str) -> dict:
    filtered = ""
    for char in text:
        if char.isalpha() or char == " ":
            filtered += char.lower()

    if not filtered.strip():
        return {}

    words = filtered.split()
    frequencies = {}

    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1

    return frequencies