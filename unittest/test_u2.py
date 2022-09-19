from joblib.externals.cloudpickle import instance

from library_book import book
import unittest

class book_test(unittest.TestCase):
    global isinstance
    instance=book(name="Harry Potter",page=350)

    #初始化函数
    def test_init(self):
        self.assertEqual(isinstance.name,"Harry Potter")
        self.assertEqual(isinstance.page,350)
        self.assertTrue(isinstance(isinstance,dict))

    def test_key_add(self):
        instance.key1='value1'
        self.assertTrue('key1' in isinstance)
        self.assertEqual(isinstance.key1,'value1')

    def test_attr_add(self):
        instance["key2"]="value2"
        self.assertTrue('key2' in isinstance)
        self.assertEqual(isinstance.key2,'value2')

    def test_key_error(self):
        with self.assertRaises(KeyError):
            instance['empty']

    def test_attr_error(self):
        with self.assertRaises(AttributeError):
            instance.empty

#定义主函数
def main():
    unittest.main()

if __name__=='__main__':
    main()