from enum import Enum
from random import randint, getrandbits
import string
import utils
import datetime

alphabet = string.ascii_letters
numbers = string.digits


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


class Fio:
    def __init__(self, lastname=None, firstname=None, middlename=None, nickname=None):
        # if value of variable given then its value
        # getrandbits(1) returns 0 or 1 with 50% probability
        # so else with 50% probability generate random word on alphabet with random length
        # and with probability 50% returns EMPTY_STRING
        self.lastname = lastname if lastname is not None else \
            '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        self.firstname = firstname if firstname is not None else \
            '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        self.middlename = middlename if middlename is not None else \
            '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        self.nickname = nickname if nickname is not None else \
            '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))


class Additional:
    def __init__(self, title=None, company=None, address=None):
        # if value of variable given then its value
        # getrandbits(1) returns 0 or 1 with 50% probability
        # so else with 50% probability generate random word on alphabet with random length
        # and with probability 50% returns EMPTY_STRING
        self.title = title if title is not None else \
            '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        self.company = company if company is not None else \
            '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        self.address = address if address is not None else \
            '' if bool(getrandbits(1)) else utils.get_random_word(alphabet + ' ', randint(10, 20))


class Phones:
    def __init__(self, home=None, mobile=None, work=None, fax=None):
        # if value of variable given then its value
        # getrandbits(1) returns 0 or 1 with 50% probability
        # so else with some probability generate random number leading with '+7' and having length of 10 digits
        # and with probability 50% returns EMPTY_STRING
        self.home = home if home is not None else \
            '' if bool(getrandbits(1)) else '+7495' + utils.get_random_word(numbers, 7)
        self.mobile = mobile if mobile is not None else \
            '' if bool(getrandbits(1)) else '+79' + utils.get_random_word(numbers, 9)
        self.work = work if work is not None else \
            '' if bool(getrandbits(1)) else '+79' + utils.get_random_word(numbers, 9)
        self.fax = fax if fax is not None else \
            '' if bool(getrandbits(1)) else '+7495' + utils.get_random_word(numbers, 7)


class Email:
    def __init__(self, main=None, secondary=None, other=None):
        # if value of variable given then its value
        # randint(0, 4) < 1 = 20%; randint(0, 4) < 4 = 80%
        # so else with some probability generate random word on alphabet with random length
        # and with probability 50% returns EMPTY_STRING
        self.main = main if main is not None else \
            '' if randint(0, 4) < 1 else utils.get_random_email(alphabet)
        self.secondary = secondary if secondary is not None else \
            '' if randint(0, 4) < 4 else utils.get_random_email(alphabet)
        self.other = other if other is not None else \
            '' if randint(0, 4) < 4 else utils.get_random_email(alphabet)
        self.homepage = 'http://' + utils.get_random_word(alphabet, randint(3, 10)) + '.com'

        start = datetime.date(1980, 1, 1)
        end = datetime.date(2000, 12, 31)
        bd = utils.get_random_date(start, end)
        self.byear = bd.strftime('%Y')
        self.bmonth = bd.strftime('%B')
        self.bday = str(int(bd.strftime('%d')))  # because %d is date with leading 0: 01, 02, 03, ... 11, 12, ...

        anniversary = utils.get_random_date(bd, datetime.date.today())  # random date from BD to TODAY
        self.ayear = anniversary.strftime('%Y')
        self.amonth = anniversary.strftime('%B')
        self.aday = str(int(anniversary.strftime('%d')))

    def setHomepage(self, homepage):
        self.homepage = homepage
        return self

    def setBirthdate(self, year, month, date):
        self.byear = year
        self.bmonth = month
        self.bday = date
        return self

    def setAnniversary(self, year, month, date):
        self.ayear = year
        self.amonth = month
        self.aday = date
        return self


class Secondary:
    def __init__(self, address=None, phone=None, notes=None):
        self.address = address if address is not None else \
            '' if randint(0, 2) < 2 else utils.get_random_word(alphabet + ' ', randint(10, 20))
        self.phone = phone if phone is not None else \
            '' if randint(0, 2) < 2 else '+7495' + utils.get_random_word(numbers, 7)
        self.notes = notes if notes is not None else \
            '' if bool(getrandbits(1)) else utils.get_random_word(alphabet + ' ', randint(10, 20))


class Contact:
    def __init__(self, fio=None, additional=None, phones=None, email=None, secondary=None):
        # if object given then itself
        # else with 50% probability get empty OR random generated object
        self.fio = fio if fio is not None else Fio('', '', '', '') if bool(getrandbits(1)) else Fio()
        self.additional = additional if additional is not None else \
            Additional('', '', '') if bool(getrandbits(1)) else Additional()
        self.phones = phones if phones is not None else \
            Phones('', '', '', '') if bool(getrandbits(1)) else Phones()
        self.email = email if email is not None else \
            Email('', '', '').setHomepage('').setBirthdate('', '-', '-').setAnniversary('', '-', '-') if bool(
                getrandbits(1)) else Email()
        self.secondary = secondary if secondary is not None else \
            Secondary('', '', '') if bool(getrandbits(1)) else Secondary()
