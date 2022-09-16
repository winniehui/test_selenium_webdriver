from selenium import webdriver
import time

# the browser basic operation:  back, forward, refresh, quit
driver = webdriver.Chrome()
driver.get("https://baidu.com")

time.sleep(2)
driver.get("https://news.baidu.com")

time.sleep(2)
driver.back()

time.sleep(2)
driver.forward()

time.sleep(2)
driver.refresh()

time.sleep(2)
driver.quit()


