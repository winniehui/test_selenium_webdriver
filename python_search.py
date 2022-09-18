from selenium import webdriver
import time

dr=webdriver.Chrome()
dr.get("https://www.python.org/")

time.sleep(1)

JS1="document.title='XXXXXXX';"
#dr.execute_script(JS1)

# 弹框显示现在的标题
time.sleep(2)
JS2=r"alert($(document).attr('title'));"
print("1111")
dr.execute_script(JS2)
print("222")
time.sleep(2)

dr.find_element_by_id("id-search-field").send_keys("pycon")
dr.find_element_by_id("submit").click()
time.sleep(2)

dr.quit()
