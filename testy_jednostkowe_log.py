def is_palindrome(tekst:str)->bool:
    cleaned = tekst.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
