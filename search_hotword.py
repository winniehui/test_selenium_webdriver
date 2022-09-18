from selenium import webdriver
from selenium.webdriver.common.by import By

dr=webdriver.Chrome()
dr.get('http://top.baidu.com/')

hw_dict = []

for i in range(10):
    xpath_1='//*[@id="hot-list"]/li["+str(i+1)+"]/a[1]'
    value = dr.find_element(By.XPATH, xpath_1).get_attribute('title')
    hw_dict.append(value)

keyword=hw_dict[0]

URL='https://www.toutiao.com/search/?keyword=%s' %keyword
dr.get(URL)

