from pages.elements_page import ElementsPage
from pages.accordian import AccordionPage
import time

def test_visible_accordion(browser):
       accordion_page = AccordionPage(browser)

       accordion_page.visit()

       assert accordion_page.sct_element.visible()
       accordion_page.hd_element.click()
       time.sleep(3)
       assert not accordion_page.sct_element.visible()

def test_not_visible_icon(browser):
       accordion_page = AccordionPage(browser)

       accordion_page.visit()

       assert not accordion_page.chk1_element.visible()
       assert not accordion_page.chk2_element.visible()
       assert not accordion_page.chk3_element.visible()