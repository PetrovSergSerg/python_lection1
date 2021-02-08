# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from group import Group
from user import User


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        self.open_groups_page(wd)
        group = Group()
        self.create_new_group(wd, group)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_handled_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        self.open_groups_page(wd)
        group = Group(name='any group', header='any header', footer='any footer')
        self.create_new_group(wd, group)
        self.return_to_groups_page(wd)
        self.logout(wd)

    def test_add_random_group(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, User.ADMIN)
        self.open_groups_page(wd)
        group = Group().set_random_parameters()
        self.create_new_group(wd, group)
        self.return_to_groups_page(wd)
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

    def open_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

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

    def return_to_groups_page(self, wd):
        wd.find_element_by_link_text("groups").click()

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
