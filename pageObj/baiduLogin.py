#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/2/1 13:44
# @Author: wei.zhang
# @File : baiduLogin.py
# @Software: PyCharm
from basefactory import webdriver


class LoginPage():
    def __init__(self, webdriver_opr):
        self.webdriver_opr = webdriver(webdriver_opr)

    def Wait_login_elements_visible(self):
        """
        等待手机号登录元素出现
        :return:
        """
        _isOK, _strlog = self.webdriver_opr.web_implicitly_wait(type='css',
                                                                locator='#root > div > div.bodyContent___3mJlP > div.mainBox___3uHai > div > div.main___3lcbD > div > div.headBox___2WQWr > div > img',
                                                                time=5)
        return _isOK, _strlog

    def Click_phone_number_login(self):
        """
        点击手机号登录
        :return:
        """
        _isOK, _strLog = self.webdriver_opr.element_click(type='css',
                                                          locator='#root > div > div.bodyContent___3mJlP > div.mainBox___3uHai > div > div.main___3lcbD > div > div.headBox___2WQWr > div > img')
        return _isOK, _strLog
