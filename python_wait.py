from selenium import webdriver

dr=webdriver.Chrome()
dr.implicitly_wait(30)  # 隐式等待，最长等30s
dr.get('https://www.csdn.net/')

print(dr.find_element_by_link_text('后端').get_attribute('href'))

dr.quit()
