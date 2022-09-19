import unittest

#继承类，编写单元测试
class calc(unittest.TestCase):

    #初始化函数
    def setUp(self):
        print("unittest start")

    #结束函数
    def tearDown(self):
        print("part of unittest end")

    #具体测试部分
    def test_add(self):
        result= 1+1
        self.assertEqual(2,result)
    def test_minus(self):
        result= 4-1
        self.assertEqual(3,result)

#定义主函数
def main():
    unittest.main()

if __name__=='__main__':
    main()