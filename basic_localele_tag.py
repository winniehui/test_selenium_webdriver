from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_tag_name("input").send_keys("selenium")
time.sleep(2)
driver.quit()
