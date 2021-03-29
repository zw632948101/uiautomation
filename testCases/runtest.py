#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/10 10:35 
# @Author : wei.zhang
# @File : runtest.py
# @Software: PyCharm

import unittest
from Util.fileDirConfig.getfiledir import CASEDIR, REPORTDIR
from BeautifulReport import BeautifulReport


class Test_run(object):

    def __init__(self):
        self.suit = unittest.TestSuite()
        self.load = unittest.TestLoader()
        self.suit.addTest(self.load.discover(CASEDIR, pattern="test_*.py", top_level_dir=None))
        self.runner = unittest.TextTestRunner()
        run = BeautifulReport(self.suit)
        run.report(report_dir=REPORTDIR, filename='testCase', description="世界农场APP V1.2.7 接口测试")


if __name__ == "__main__":
    test_run = Test_run()
