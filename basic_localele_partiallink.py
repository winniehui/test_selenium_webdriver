from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "新").click()
time.sleep(2)
driver.back()

time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "地").click()
driver.back()

time.sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, "视").click()
driver.back()

time.sleep(2)
driver.quit()
