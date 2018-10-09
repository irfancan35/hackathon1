from BasePage import BasePage
from Locators import *

class HomePage(BasePage):
    def home_click(self):
        element = self.browser.find_element(*HomePageLocator.home)
        element.click()