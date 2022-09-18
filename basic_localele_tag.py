from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element(By.TAG_NAME,"input").send_keys("selenium")
time.sleep(2)
driver.quit()
