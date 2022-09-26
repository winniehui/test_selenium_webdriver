from selenium import webdriver
import time
import os

driver_path = "D:\\browserDriver\\"
# browser参数值从jenkins传递过来
b_type = os.getenv("browser")

if b_type == "chrome":
    dr = webdriver.Chrome(driver_path + "chromedriver.exe")
elif b_type == "firefox":
    dr = webdriver.Firefox(executable_path = driver_path + "geckodriver.exe")

time.sleep(3)

#link的参数值从jenkins传递过来
geturl = os.getenv("link")
dr.get(geturl)
#dr.get('http://cal.apple886.com/')

time.sleep(5)

dr.quit()