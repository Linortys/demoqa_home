from selenium.webdriver.common.by import By
class BasePage:

    def __init__(self, driver, base_url, locator=''):
        self.driver = driver
        self.base_url = base_url
        self.locator = locator

    def visit(self):
        return self.driver.get(self.base_url)

    def get_url(self):
        return self.driver.current_url

    def find_element(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.locator)

    def equal_url(self):
        if self.get_url() == self.base_url:
             return True
        else:
             return False

