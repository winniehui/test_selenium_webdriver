from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

time.sleep(2)
driver.find_element_by_link_text("新闻").click()
driver.back()

time.sleep(2)
driver.find_element_by_link_text("地图").click()
driver.back()

time.sleep(2)
driver.find_element_by_link_text("视频").click()
driver.back()

time.sleep(2)
driver.quit()
