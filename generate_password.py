import string
import random
from typing import List


def generate_random_password(lenght: int, with_letters: bool = True, with_digits: bool = True, with_symbols: bool = True) -> str:
    password : List[str] = []
    characters : List[str]
    letters : str = ""
    digits : str = ""
    symbols : str = ""
    
    if lenght <= 0:
        return ""
        
    if not with_letters and not with_digits and not with_symbols:
        return ""
    
    if with_letters:
        letters = string.ascii_letters
        
    if with_digits:
        digits = string.digits
        
    if with_symbols:
        symbols = "!@#$%^&*()"
    
    characters = list(letters + digits + symbols)

    random.shuffle(characters)

    for i in range(lenght):
        password.append(random.choice(characters))

    random.shuffle(password)
    
    return str("".join(password))
