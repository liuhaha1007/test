from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ResContactPage(BaseAction):
    large_title = By.ID, "com.android.contacts:id/large_title"
    def get_large_title(self):
        return self.find_element(self.large_title).text