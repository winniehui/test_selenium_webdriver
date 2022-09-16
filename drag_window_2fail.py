from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.toutiao.com/")

driver.save_screenshot("save_1.png")

ac = driver.find_element_by_xpath("//u1[@infinite-scroll-disabled]/li[last()]")
ActionChains(driver).move_to_element(ac).perform()

time.sleep(2)
driver.save_screenshot("save_2.png")

