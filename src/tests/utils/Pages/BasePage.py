
import pytest
from selenium import webdriver

class BasePage(object):

    def __init__(self, browser):
        self.browser = browser


    def open(self):
        self.browser.get("https://www.agoda.com/")

