from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_class_name("s_ipt").send_keys("selenium")

driver.find_element_by_id("su").click()

time.sleep(2)
driver.quit()
