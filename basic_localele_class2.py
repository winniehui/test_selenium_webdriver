from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element(By.CLASS_NAME, "s_ipt").send_keys("selenium")

elements = driver.find_elements(By.TAG_NAME, 'input')
print(elements)
for element in elements:
    className = element.get_attribute('class')
    print(className)
    if className == 'bg s_btn':
        subscript = elements.index(element)
elements[subscript].click()

time.sleep(2)
driver.quit()

