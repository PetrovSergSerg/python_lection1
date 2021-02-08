# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact
from user import User


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        empty_contact = Contact()  # generate empty contact
        self.create_new_contact(wd, empty_contact)
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_random_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        random_contact = Contact().set_random_parameters()  # generate fully random Contact
        self.create_new_contact(wd, random_contact)
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_full_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        empty_contact = Contact(lastname='aaa', firstname='bbb', middlename='ccc', nickname='ddd', title='kkk',
                                company='lll', address='mmm', home='111', mobile='222', work='333', fax='444',
                                main='a@a.ru', secondary='b@b.ru', other='c@c.ru', homepage='http://', byear='1994',
                                bmonth='April', bday='15', ayear='2003', amonth='September', aday='4', address2='xxx',
                                phone='777', notes='zzz')
        self.create_new_contact(wd, empty_contact)
        self.return_to_home_page(wd)
        self.logout(wd)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, user: User):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user.login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user.password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def create_new_contact(self, wd, contact: Contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.nickname)

        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").send_keys(contact.address)

        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").send_keys(contact.fax)

        wd.find_element_by_name("email").send_keys(contact.main)
        wd.find_element_by_name("email2").send_keys(contact.secondary)
        wd.find_element_by_name("email3").send_keys(contact.other)
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

        selector = Select(wd.find_element_by_name("bday"))
        selector.select_by_visible_text(contact.bday)
        selector = Select(wd.find_element_by_name("bmonth"))
        selector.select_by_visible_text(contact.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.byear)

        selector = Select(wd.find_element_by_name("aday"))
        selector.select_by_visible_text(contact.aday)
        selector = Select(wd.find_element_by_name("amonth"))
        selector.select_by_visible_text(contact.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.ayear)

        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").send_keys(contact.phone)
        wd.find_element_by_name("notes").send_keys(contact.notes)

        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
