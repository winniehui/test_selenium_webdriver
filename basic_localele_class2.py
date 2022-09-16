from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")

driver.find_element_by_class_name("s_ipt").send_keys("selenium")

elements = driver.find_elements_by_tag_name('input')
print(elements)
for element in elements:
    className = element.get_attribute('class')
    print(className)
    if className == 'bg s_btn':
        subscript = elements.index(element)
elements[subscript].click()

time.sleep(2)
driver.quit()

