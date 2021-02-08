import utils
from random import randint
import string

alphabet = string.ascii_letters


class Group:
    def __init__(self, name='', header='', footer=''):
        self.name = name
        self.header = header
        self.footer = footer

    def set_random_parameters(self):
        self.name = '' if randint(0, 4) < 1 else utils.get_random_word(alphabet, randint(3, 10))
        self.header = '' if randint(0, 4) < 1 else utils.get_random_word(alphabet + ' ', randint(10, 20))
        self.footer = '' if randint(0, 4) < 1 else utils.get_random_word(alphabet + ' ', randint(10, 20))
        return self
