from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_css_selector("#kw").send_keys("selenium")
driver.find_element_by_css_selector("#su").click()

time.sleep(2)
driver.quit()
