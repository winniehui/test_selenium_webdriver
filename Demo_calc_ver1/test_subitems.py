from selenium.webdriver.common.by import By
import os
from Setup import *

def testLogin():
    print("Login Successful")

def testLogoff():
    print("Logoff Successful")

def testSub():
    p_a = os.getenv("the first number")
    p_b = os.getenv("the second number")
    path_a = '//*[@id="simple' + p_a + '"]'
    path_b = '//*[@id="simple' + p_b + '"]'
    path_sub = '//*[@id="simpleSubtr"]'
    path_eq = '//*[@id="simpleEqual"]'

    dr = t_login()

    dr.find_element(By.XPATH, path_a).click()
    time.sleep(1)

    dr.find_element(By.XPATH, path_sub).click()
    time.sleep(1)

    dr.find_element(By.XPATH, path_b).click()
    time.sleep(1)

    dr.find_element(By.XPATH, path_eq).click()
    time.sleep(1)

    result_text = 4
    time.sleep(1)

    t_logoff(dr)

    c = int(p_a) - int(p_b)
    print("c: ", c)


    assert c == result_text