from pages.demoqa import DemoQa
from conftest import browser
from components.components import WebElement
from pages.elements_page import ElementsPage
from pages.modal_dialogs import ModelPage
import time

def test_modal_elements(browser):
    modal_page = ModelPage(browser)
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    modal_page.visit()
    assert modal_page.link.check_count(count=5)


def test_navigation_modal(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)
    modal_page = ModelPage(browser)

    modal_page.visit()
    modal_page.update()

    modal_page.hdr_element.click()
    time.sleep(3)
    browser.back()
    browser.set_window_size(900, 400)
    browser.forward()
    browser.set_window_size(1000, 1000)
    assert demo_qa_page.equal_url()
    assert demo_qa_page.icon.visible()