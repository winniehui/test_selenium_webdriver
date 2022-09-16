from selenium import webdriver
import time

# localtion via xpath
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_xpath(r'//*[@id="kw"]').send_keys("selenium")

driver.find_element_by_id("su").click()
time.sleep(2)
driver.quit()

