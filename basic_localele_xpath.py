from selenium import webdriver
import time

# localtion via xpath
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element(By.XPATH, r'//*[@id="kw"]').send_keys("selenium")

driver.find_element(By.ID, "su").click()
time.sleep(2)
driver.quit()

