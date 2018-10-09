from selenium import webdriver
import pytest
import sys
from utils.basetest import BaseTest
from utils.Pages.BasePage import *
from utils.Pages.HomePage import *
import unittest
import time
from utils.Setup import *

@pytest.mark.incremental
class TestMain(BaseTest):

    def test_sample(self):
        basePage = BasePage(self.driver)
        basePage.open()
        homePage = HomePage(self.driver)
        homePage.home_click()
        time.sleep(2)

