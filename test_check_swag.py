from selenium.webdriver.common.by import By
from conftest import browser
from pages.swag_labs import SwagLabs
from pages.base_page import BasePage


def user_name_find(browser):
    swag_lab = SwagLabs(browser)
    swag_lab.visit()
    swag_lab.find_element(locator= 'user-name')

def pass_find(browser):
    swag_lab = SwagLabs(browser)
    swag_lab.visit()
    swag_lab.find_element(locator= 'password')

def test_icon(browser):
    swag_lab = SwagLabs(browser)
    swag_lab.visit()
    assert swag_lab.exist_icon()

