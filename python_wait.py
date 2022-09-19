from selenium import webdriver
from selenium.webdriver.common.by import By

dr=webdriver.Chrome()
dr.implicitly_wait(30)  # 隐式等待，最长等30s
dr.get('https://www.csdn.net/')

print(dr.find_element(By.LINK_TEXT, '后端').get_attribute('href'))

dr.quit()
