#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/12 16:17 
# @Author : wei.zhang
# @File : runLevel.py
# @Software: PyCharm
from Util.Config import config


class RunLevel(object):
    @staticmethod
    def skip_case(case_level):
        """
        判断是否需要跳过用例
        :param level: 用例等级
        :return: 返回布尔值
        """
        run_level = config.get('RUN_LEVEL')
        if 0 < run_level <= case_level:
            return True
        return False
