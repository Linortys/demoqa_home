from pages.demoqa import DemoQa
from conftest import browser
from pages.elements_page import ElementsPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_find_text_foot(browser):
    footer_find_text = DemoQa(browser)
    footer_find_text.visit()
    footer_text = footer_find_text.footer.get_text()
    assert footer_text == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_find_text_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    demo_qa_page.btn_elements.click()
    assert elements_page.equal_url()

    assert str(elements_page.center_element.get_text()) == 'Please select an item from left to start practice.'

