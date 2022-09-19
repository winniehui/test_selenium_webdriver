import HtmlTestRunner
import unittest

directory=r"[dir]"

#遍历测试文件
def createsuite():
    #创建unittest实例
    test_suit=unittest.TestSuite()

    discover=unittest.defaultTestLoader.discover(directory,pattern='*_unittest.py',top_level_dir=None)

    #计数器
    counter=0
    for i in discover:
        counter+=1
        print("已发现{}个测试实例需要执行".format(counter))
        for j in i:
            #添加测试单元
            test_suit.addTests(j)

    #返回
    return test_suit

#定义执行函数
def main():
    #输出HTML文件的位置
    filename=r"D:\python document\pythonProject\test_selenium_webdriver\unittest\result.html"
    #以二进制方式打开文件
    f=open(filename,'wb')
    #使用HTMLTestRunner运行
    runner=HtmlTestRunner.HTMLTestRunner(stream=f,title='测试报告',description='实例执行情况：')
    #执行
    runner.run(createsuite())
    #关闭文件流
    f.close()

#只在主动运行的时候才执行
if __name__=='__main__':
    main()