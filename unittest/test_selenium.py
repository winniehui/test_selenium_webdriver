from selenium import webdriver

dr = webdriver.Chrome(executable_path=r"D:\python document\pythonProject\test_selenium_webdriver\chromedriver.exe")

dr.get("https://pypi.org/search/")

assert "Python" in dr.title

dr.close()