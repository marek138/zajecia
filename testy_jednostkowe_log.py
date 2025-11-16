def is_palindrome(tekst:str)->bool:
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
