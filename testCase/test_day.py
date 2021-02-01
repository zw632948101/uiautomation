#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/29 17:40
# @Author: wei.zhang
# @File : test_day.py
# @Software: PyCharm
import time

from basefactory import browser


class TestDay(browser):
    def test_dar(self):

        istrue, driver = self.open_url(locator='http://www.baidu.com')
        time.sleep(5)
        browser.close_browser()

