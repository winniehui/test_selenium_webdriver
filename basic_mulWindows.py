from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("http://baidu.com")

time.sleep(2)
# 使用多个窗口
# 打开多个页面，地址栏下有多个标签
JS1 = 'window.open("https://www.sogou.com");'
driver.execute_script(JS1)

time.sleep(2)
JS2 = 'window.open("https://fanyi.youdao.com/");'
driver.execute_script(JS2)

time.sleep(2)
driver.quit()

