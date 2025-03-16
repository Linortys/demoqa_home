from selenium.webdriver.common.by import By
from conftest import browser
from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    swag_lab = SwagLabs(browser)
    swag_lab.visit()
    assert swag_lab.exist_icon()
    swag_lab.user_name_find()
    swag_lab.pass_find()
