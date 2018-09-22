from time import sleep

from base.base_driver import init_driver
from page.page import Page


class TestNewContact:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
    def test_new_contact(self):
        name = '阿好'
        phone = "18503080303"

        self.page.contact_page.click_new_contact()
        self.page.new_contact_page.click_local_save()
        self.page.new_contact_page.input_name(name)
        self.page.new_contact_page.input_phone(phone)
        self.page.new_contact_page.click_back()


        assert name == self.page.result_contact_page.get_large_title()


