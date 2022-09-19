from selenium import webdriver
import time

from selenium.webdriver.common.by import By

dr=webdriver.Chrome()
dr.get("https://www.python.org/")

time.sleep(2)
JS1 = "document.title='happy pigpig';"
dr.execute_script(JS1)

time.sleep(2)
dr.find_element(By.ID, "id-search-field").send_keys("pycon")
dr.find_element(By.ID, "submit").click()

#通过CSS样式查找
dr.find_element(By.CSS_SELECTOR, r'#content>div>section>form>u1>li:nth-child(1)>h3>a').click()

dr.save_screenshot("save.png")

dr.quit()
