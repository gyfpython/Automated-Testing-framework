#!coding=utf-8
import selenium
import os
import time
import unittest

class LoginTests(unittest.TestCase):
    login, my_account, driver = None, None, None

    def setUp(self):
        print 'test start'

    def tearDown(self):
        # lcc.log_info("Finished running test ")
        capture_screenshot(self.driver)
        self.driver.quit()
    @classmethod
    def setUpClass(self):
        # lcc.log_info("Inside setup")
        self.driver = webdriver.Chrome()
        self.login = LoginPage(driver=self.driver)
        self.my_account = MyAccountPage(driver=self.driver)
