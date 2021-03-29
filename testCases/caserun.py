#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/9 15:40 
# @Author : wei.zhang
# @File : caserun.py
# @Software: PyCharm

import unittest
from common.factory import Factory
from ddt import ddt, data


@ddt
class TestCaseRun(unittest.TestCase):
    fac = Factory()
    excu_cases = fac.init_execute_case()

    @data(*excu_cases)
    def test_run(self, acases):
        for key, cases in acases.items():
            for case in cases:
                isOK, result = self.fac.execute_keyword(keyword=case['keyword'],
                                                        type=case['type'],
                                                        locator=case['locator'],
                                                        index=case['index'],
                                                        input=case['input'],
                                                        check=case['check'],
                                                        time=case['time']
                                                        )
                if isOK:
                    print(result)
                else:
                    raise Exception(result)
