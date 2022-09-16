from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://python.org")
time.sleep(2)
driver.maximize_window()

time.sleep(2)

# 拖动窗口
#执行javaScript代码
JS = "window.scrollTo(10000,document.body.scrollHeight)"
driver.execute_script(JS)

time.sleep(2)
driver.quit()

