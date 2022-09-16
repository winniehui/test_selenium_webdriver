from selenium import webdriver
import time
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()

# get all the cookie
cookies = driver.get_cookies()

# 返回字典的key为BAIDUID的cookie
cookie = driver.get_cookie("BAIDUID")
print(cookies, "\n")
print(cookie)

# delete all the cookie message
driver.delete_all_cookies()


driver.quit()
