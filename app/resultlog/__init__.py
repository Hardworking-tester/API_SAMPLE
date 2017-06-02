# encoding:utf-8

from selenium import webdriver
import unittest


class classname(unittest.TestCase):
    def setUp(self):
        pass

    def testCase(self):
        pass

    def tearDown(self):
        pass


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(classname("testCase"))
    runner = unittest.TextTestRunner()
    runner.run(suite)