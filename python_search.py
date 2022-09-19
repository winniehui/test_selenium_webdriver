from selenium import webdriver
import time

from selenium.webdriver.common.by import By

dr=webdriver.Chrome()
dr.get("https://www.python.org/")

time.sleep(1)

JS1="document.title='XXXXXXX';"
#dr.execute_script(JS1)

# 弹框显示现在的标题
time.sleep(2)
JS2=r"alert($(document).attr('title'));"

dr.execute_script(JS2)

time.sleep(2)

dr.find_element(By.ID, "id-search-field").send_keys("pycon")
dr.find_element(By.ID, "submit").click()
time.sleep(2)

dr.quit()
