# coding-utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://localhost:8080")
driver.fullscreen_window()
content = driver.find_element_by_xpath("/html/body/div/div/div").text
driver.refresh
content1 = driver.find_element(By.XPATH,"/html/body/div/div/div").text
print (content)
print (content1)
print (driver.title)
driver.quit()