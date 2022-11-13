from string import ascii_letters
from string import digits
from random import sample


def get_random_password(n: int = 8) -> str:
    alphabet = list(ascii_letters) + list(digits)
    return ''.join(sample(alphabet, n))
    # TODO написать функцию генерации случайных паролей


print(get_random_password())
