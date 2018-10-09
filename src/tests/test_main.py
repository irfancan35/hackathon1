from selenium import webdriver
import pytest
import sys
from utils.basetest import BaseTest
from utils.Pages.BasePage import BasePage
import unittest
from utils.Setup import *

@pytest.mark.incremental
class TestMain(BaseTest):

    def test_sample(self):
        basePage = BasePage(self.driver)
        basePage.open()

