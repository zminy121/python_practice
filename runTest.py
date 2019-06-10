import unittest


testDir = r'E:\python_project\automalize_test'
dicover = unittest.defaultTestLoader.discover(testDir,pattern='test*.py')


# import testAdd
# import testSub
# suite = unittest.TestSuite()
# suite.addTest(testAdd.MyTest('test_add1'))
# suite.addTest(testAdd.MyTest('test_add2'))
# suite.addTest(testSub.MyTest('test_sub1'))
# suite.addTest(testSub.MyTest('test_sub2'))

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    # runner.run(suite)
    runner.run(dicover)