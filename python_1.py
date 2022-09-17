from selenium import webdriver
import time

# 启动浏览器，打开页面
dr = webdriver.Chrome()
dr.get("https://www.python.org/")

# 修改标题
time.sleep(1)
JS1 = "document.title='修改弹窗标题：猪仔茂茂系叻叻猪';"
dr.execute_script(JS1)

# 弹窗标题
time.sleep(1)
JS2=r"alert($(document).attr('title'));"
dr.execute_script(JS2)
time.sleep(3)

# 退出
dr.quit()
