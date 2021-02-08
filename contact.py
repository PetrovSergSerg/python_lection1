from random import randint, getrandbits
import string
import utils
import datetime

alphabet = string.ascii_letters
numbers = string.digits


class Contact:
    def __init__(self, lastname='', firstname='', middlename='', nickname='',
                 title='', company='', address='', home='', mobile='', work='', fax='',
                 main='', secondary='', other='', homepage='', byear='', bmonth='-', bday='-',
                 ayear='', amonth='-', aday='-', address2='', phone='', notes=''):
        self.lastname = lastname
        self.firstname = firstname
        self.middlename = middlename
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.main = main
        self.secondary = secondary
        self.other = other
        self.homepage = homepage
        self.byear = byear
        self.bmonth = bmonth
        self.bday = bday
        self.ayear = ayear
        self.amonth = amonth
        self.aday = aday
        self.address2 = address2
        self.phone = phone
        self.notes = notes

    def set_random_parameters(self):
        # getrandbits(1) returns 0 or 1 with 50% probability
        # with 50% probability generate random word on alphabet with random length
        # and with probability 50% returns EMPTY_STRING
        self.lastname = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        self.firstname = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        self.middlename = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        self.nickname = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))

        # getrandbits(1) returns 0 or 1 with 50% probability
        # with 50% probability generate random word on alphabet with random length
        # and with probability 50% returns EMPTY_STRING
        self.title = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        self.company = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet, randint(3, 10))
        self.address = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet + ' ', randint(10, 20))

        # 30% probability to be empty value
        self.home = '' if randint(0, 2) < 1 else '+7495' + utils.get_random_word(numbers, 7)
        # 10% probability to be empty value
        self.mobile = '' if randint(0, 9) < 1 else '+79' + utils.get_random_word(numbers, 9)
        # 50% probability to be empty value
        self.work = '' if bool(getrandbits(1)) else '+79' + utils.get_random_word(numbers, 9)
        # 10% probability to be empty value
        self.fax = '' if randint(0, 9) < 1 else '+7495' + utils.get_random_word(numbers, 7)

        # randint(0, 4) < 1 = 20%; randint(0, 4) < 4 = 80%
        # with some probability generate random word on alphabet with random length
        self.main = '' if randint(0, 4) < 1 else utils.get_random_email(alphabet)
        self.secondary = '' if randint(0, 4) < 4 else utils.get_random_email(alphabet)
        self.other = '' if randint(0, 4) < 4 else utils.get_random_email(alphabet)
        self.homepage = '' if bool(getrandbits(1)) \
            else 'http://' + utils.get_random_word(alphabet, randint(3, 10)) + '.com'

        start = datetime.date(1980, 1, 1)
        end = datetime.date(2000, 12, 31)
        bd = utils.get_random_date(start, end)  # get random date between given dates
        if bool(getrandbits(1)):  # 50% probability set birthdate
            self.byear = bd.strftime('%Y')  # get year from this date
            self.bmonth = bd.strftime('%B')  # get month in format April, January, ...
            self.bday = str(int(bd.strftime('%d')))  # because %d is date with leading 0: 01, 02, 03, ... 11, 12, ...

        if bool(getrandbits(1)):  # 50% probability to generate anniversary date
            anniversary = utils.get_random_date(bd, datetime.date.today())  # random date from BD to TODAY
            self.ayear = anniversary.strftime('%Y')
            self.amonth = anniversary.strftime('%B')
            self.aday = str(int(anniversary.strftime('%d')))

        # randint(0, 2) < 2 = 66%; getrandbits(1) returns 0 or 1 with 50% probability
        # with some probability generate random word on alphabet with random length
        self.address2 = '' if randint(0, 2) < 2 else utils.get_random_word(alphabet + ' ', randint(10, 20))
        self.phone = '' if randint(0, 2) < 2 else '+7495' + utils.get_random_word(numbers, 7)
        self.notes = '' if bool(getrandbits(1)) else utils.get_random_word(alphabet + ' ', randint(10, 20))

        return self
