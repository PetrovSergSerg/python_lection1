import datetime
from random import randint


def get_random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=randint(0, int((end - start).total_seconds())),
    )


def get_random_word(alphabet: str, length: int):
    """Generate a random word on alphabet with given length"""
    random_word = ''
    for i in range(length):
        random_word += alphabet[randint(0, len(alphabet) - 1)]
    return random_word


def get_random_email(alphabet: str):
    """Generate random email using function get_random_word(alphabet, length)"""
    return get_random_word(alphabet, randint(3, 10)) + '@' + get_random_word(alphabet, randint(2, 10)) + '.ru'
