from calculator import Count
from setUpTearDown import Test
import unittest



class MyTest(Test):

    def test_sub1(self):
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1, msg='不等于-1')

    def test_sub2(self):
        j = Count(4,3)
        self.assertEqual(j.sub(), 1, msg='不等于1')

if __name__ == '__main__':
    unittest.main()