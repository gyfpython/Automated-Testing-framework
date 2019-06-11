# coding=utf-8

from selenium import webdriver
from page.homePage import HomePage

def getTitle():
    driver = webdriver.Chrome()
    HomePage().getHomePage(driver)
    print (driver.title)
    HomePage().quitPage(driver)


if __name__ == "__main__":
    getTitle()