from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

time.sleep(2)
driver.find_element_by_partial_link_text("新").click()
time.sleep(2)
driver.back()

time.sleep(2)
driver.find_element_by_partial_link_text("地").click()
driver.back()

time.sleep(2)
driver.find_element_by_partial_link_text("视").click()
driver.back()

time.sleep(2)
driver.quit()
