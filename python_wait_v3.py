from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

dr = webdriver.Chrome()
dr.implicitly_wait(10)
dr.get('https://www.csdn.net/')

locator = (By.LINK_TEXT, u'后端')
try:
    WebDriverWait(dr,20,0.5).until(EC.presence_of_element_located(locator))
    #WebDriverWait(driver=self.dr,timeout=20,poll_frequency=0.5,ignored_exceptions=None)
finally:
    print(dr.find_element_by_link_text('后端').get_attribute('href'))

dr.quit()
