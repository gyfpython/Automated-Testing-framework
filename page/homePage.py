# coding=utf-8
from config.environment import *
from utils.logfuction import Logger
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By

#loginfo = Logger('..\log\check.log',level='info')

class HomePage():
    # go to homepage
    def getHomePage(self, driver):
        #loginfo.logger.info("HomePage")
        try:
            driver.get(url)
            driver.find_element(By.XPATH,body)
            #loginfo.logger.info("success")
        except Exception as e:
            print(e)
            #loginfo.logger.error(e)

    # quit
    def quitPage(self, driver):
        driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    HomePage().getHomePage(driver)
    #loginfo.logger.info(driver.title)
    HomePage().quitPage(driver)