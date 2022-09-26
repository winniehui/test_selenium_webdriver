from selenium import webdriver
import time
import os

def t_login():
    driver_path = "D:\\browserDriver\\"
    # browser参数值从jenkins传递过来
    b_type = os.getenv("browser")

    if b_type == "chrome":
        dr = webdriver.Chrome(driver_path + "chromedriver.exe")
    elif b_type == "firefox":
        dr = webdriver.Firefox(executable_path = driver_path + "geckodriver.exe")

#    dr = webdriver.Chrome(driver_path + "chromedriver.exe")

    time.sleep(1)

    dr.get('http://cal.apple886.com/')

    time.sleep(1)

    return dr

def t_logoff(dr):
    dr.quit()
    return