# coding=utf-8
from selenium import webdriver
from page.homePage import HomePage
from config.environment import *
from selenium.webdriver.common.by import By
import unittest

class gettitle(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("start access")
        HomePage().getHomePage(self.driver)
        print("success access")

    def test_gettitle(self):
        print("get title")
        title = self.driver.title
        print("get title success")
        self.assertEqual(title, 'Hello World', msg='title error!')

    def test_getbody(self):
        print("get boody")
        pageBody = self.driver.find_element(By.XPATH, body).text
        print("get body success")
        self.assertEqual(pageBody, 'Hello World React', msg='body error!')

    def tearDown(self):
        HomePage().quitPage(self.driver)

if __name__ == "__main__":
    unittest.main()