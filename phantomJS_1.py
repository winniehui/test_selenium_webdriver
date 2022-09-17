from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

driver=webdriver.PhantomJS()
time.sleep(2)
driver.get("http://cn.bing.com/")
time.sleep(2)

title_=driver.title
print(title_)

time.sleep(2)
keywords = 'SELENIUM 自动化测试'
driver.find_element_by_id("sb_form_q").send_keys(keywords)
time.sleep(2)

driver.save_screenshot("bing_1.png")
time.sleep(2)

driver.find_element_by_id("sb_form_go").click()
time.sleep(2)
driver.save_screenshot("bing_2.png")
time.sleep(2)

driver.find_element_by_xpath("/html/body/div/ol/li/h2/a").click()
time.sleep(2)
driver.save_screenshot("bing_3.png")
time.sleep(2)

driver.quit()
