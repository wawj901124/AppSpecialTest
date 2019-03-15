import unittest


# from test import test_support
class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def clear(self):
        pass

    def getTest(self, arg1, arg2):  # 定义的函数，最终生成的测试用例的执行方法
        print(arg1, arg2)
        pass

    @staticmethod
    def getTestFunc(arg1, arg2):
        def func(self):
            self.getTest(arg1, arg2)

        return func


def __generateTestCases():
    arglists = [('arg11', 'arg12'), ('arg21', 'arg22'), ('arg31', 'arg32')]
    for args in arglists:
        setattr(MyTestCase, 'test_func_%s_%s' % (args[0], args[1]),
                MyTestCase.getTestFunc(*args))  # 通过setattr自动为TestCase类添加成员方法，方法以“test_func_”开头


__generateTestCases()
if __name__ == '__main__':
    # test_support.run_unittest(MyTestCase)
    unittest.main()
