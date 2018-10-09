from selenium import webdriver
import pytest
import sys
from Pages.basetest import BaseTest
from Pages.BasePage import BasePage
import unittest
from Pages.Setup import *

@pytest.mark.incremental
class TestMain(BaseTest):

    def test_sample(self):
        basePage = BasePage(self.driver)
        basePage.open()

