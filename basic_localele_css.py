from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("selenium")
driver.find_element(By.CSS_SELECTOR, "#su").click()

time.sleep(2)
driver.quit()
