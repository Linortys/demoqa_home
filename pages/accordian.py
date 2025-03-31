from components.components import WebElement
from pages.base_page import BasePage

class AccordionPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver,self.base_url)

        self.sct_element = WebElement(driver, '#section1Content > p')
        self.hd_element = WebElement(driver, "#section1Heading")
        self.chk1_element = WebElement(driver, "#section2Content > p:nth-child(1)")
        self.chk2_element = WebElement(driver, "#section2Content > p:nth-child(2)")
        self.chk3_element = WebElement(driver, "#section3Content > p")