from components.components import WebElement
from pages.base_page import BasePage

class ModelPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver,self.base_url)

        self.hdr_element = WebElement(driver, "#app > header > a > img")
        self.link = WebElement(driver, "#app > div > div > div > div:nth-child(1) > div > div > div:nth-child(3) > div > ul > li")