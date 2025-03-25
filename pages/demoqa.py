import pytest
from conftest import browser
from components.components import WebElement
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url ='https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.footer = WebElement(driver, '#app > footer > span')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')
        # self.element_text = WebElement(driver, '#app > div > div > div > div[2] > text()')
