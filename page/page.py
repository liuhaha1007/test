from page.contact_page import ContactPage
from page.new_contact_page import NewContactPage
from page.result_contact_page import ResContactPage


class Page:
    def __init__(self,driver):
        self.driver = driver
    @property
    def contact_page(self):
        return ContactPage(self.driver)

    @property
    def new_contact_page(self):
        return NewContactPage(self.driver)

    @property
    def result_contact_page(self):
        return ResContactPage(self.driver)
