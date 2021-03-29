#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/3/19 16:42
# @Author: wei.zhang
# @File : APPOperator.py
# @Software: PyCharm
from appium import webdriver
from Util.conf import config


class AppOperator:
    def __init__(self):
        super(AppOperator).__init__()

    def open_app(self):
        """
        打开测试APP
        :return:
        """
        desired_caps = config.get('DESIRED_CAPS')
        command_executor = config.get('COMMAND_EXECUTOR')
        driver = webdriver.Remote(command_executor, desired_caps)
        return driver
