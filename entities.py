from enum import Enum


class User(Enum):
    ADMIN = ('admin', 'secret')

    def __init__(self, login, password):
        self.login = login
        self.password = password


class Group:
    def __init__(self, name, header, footer):
        self.name = name
        self.header = header
        self.footer = footer
