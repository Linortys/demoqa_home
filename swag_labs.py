from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SwagLabs(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def user_name_find(self):
        self.find_element(locator='#user-name')

    def pass_find(self):
        self.find_element(locator='#password')