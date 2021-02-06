# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from entities import User, Group, Contact, Fio, Additional, Phones, Email, Secondary


class TestAddressbook(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        self.open_groups_page(wd)
        group = Group(name='empty group', header='', footer='')
        self.create_new_group(wd, group)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        self.open_groups_page(wd)
        group = Group(name='any name', header='header', footer='footer')
        self.create_new_group(wd, group)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        empty_contact = Contact(
            Fio('', '', '', ''),
            Additional('', '', ''),
            Phones('', '', '', ''),
            Email('', '', '').setHomepage('').setBirthdate('', '-', '-').setAnniversary('', '-', '-'),
            Secondary('', '', '')
        )
        self.create_new_contact(wd, empty_contact)
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_random_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        random_contact = Contact()  # generate fully random Contact
        self.create_new_contact(wd, random_contact)
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_full_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        empty_contact = Contact(
            Fio('aaa', 'bbb', 'ccc', 'ddd'),
            Additional('kkk', 'lll', 'mmm'),
            Phones('111', '222', '333', '444'),
            Email('a@a.ru', 'b@b.ru', 'c@c.ru')
                .setHomepage('http')
                .setBirthdate('1996', 'April', '13')
                .setAnniversary('2013', 'September', '4'),
            Secondary('f@f.ru', '777', 'xxx')
        )
        self.create_new_contact(wd, empty_contact)
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_new_contact(self, wd, contact: Contact):
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys(contact.fio.firstname)
        wd.find_element_by_name("middlename").send_keys(contact.fio.middlename)
        wd.find_element_by_name("lastname").send_keys(contact.fio.lastname)
        wd.find_element_by_name("nickname").send_keys(contact.fio.nickname)

        wd.find_element_by_name("title").send_keys(contact.additional.title)
        wd.find_element_by_name("company").send_keys(contact.additional.company)
        wd.find_element_by_name("address").send_keys(contact.additional.address)

        wd.find_element_by_name("home").send_keys(contact.phones.home)
        wd.find_element_by_name("mobile").send_keys(contact.phones.mobile)
        wd.find_element_by_name("work").send_keys(contact.phones.work)
        wd.find_element_by_name("fax").send_keys(contact.phones.fax)

        wd.find_element_by_name("email").send_keys(contact.email.main)
        wd.find_element_by_name("email2").send_keys(contact.email.secondary)
        wd.find_element_by_name("email3").send_keys(contact.email.other)
        wd.find_element_by_name("homepage").send_keys(contact.email.homepage)

        selector = Select(wd.find_element_by_name("bday"))
        selector.select_by_visible_text(contact.email.bday)
        selector = Select(wd.find_element_by_name("bmonth"))
        selector.select_by_visible_text(contact.email.bmonth)
        wd.find_element_by_name("byear").send_keys(contact.email.byear)

        selector = Select(wd.find_element_by_name("aday"))
        selector.select_by_visible_text(contact.email.aday)
        selector = Select(wd.find_element_by_name("amonth"))
        selector.select_by_visible_text(contact.email.amonth)
        wd.find_element_by_name("ayear").send_keys(contact.email.ayear)

        wd.find_element_by_name("address2").send_keys(contact.secondary.address)
        wd.find_element_by_name("phone2").send_keys(contact.secondary.phone)
        wd.find_element_by_name("notes").send_keys(contact.secondary.notes)

        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def create_new_group(self, wd, group: Group):
        wd.find_element_by_name("new").click()

        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

        wd.find_element_by_name("submit").click()

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def login(self, wd, user: User):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user.login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(user.password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

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
