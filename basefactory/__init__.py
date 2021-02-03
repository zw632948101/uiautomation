#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/29 17:32
# @Author: wei.zhang
# @File : __init__.py.py
# @Software: PyCharm

from .browseroperator import BrowserOperator
from .webdriveroperator import WebdriverOperator
from Util.Config import config

browser = BrowserOperator
webdriver = WebdriverOperator


class OpenWebdriver:
    def __init__(self):
        self.driver = None
        self.browser_opr = browser()

    def open_url(self, url=None):
        if not url:
            url = config.get('URL_UNDER_TEST')
        isOK, result = self.browser_opr.open_url(locator=url)
        return isOK, result


class Base:
    openweb = OpenWebdriver()

    def setup(self) -> None:
        isOK, result = self.openweb.open_url()
        self.result = result

    def teardown(self) -> None:
        self.openweb.browser_opr.close_browser()
