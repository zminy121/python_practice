from calculator import Count
from setUpTearDown import Test
import unittest

class MyTest(Test):
    def setUp(self):
        print('test case start')

    def tearDown(self):
        print('test case end')

    def test_add1(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5, msg='不等于5')

    def test_add2(self):
        j = Count(4,3)
        self.assertEqual(j.add(), 7, msg='不等于7')

if __name__ == '__main__':
    unittest.main()