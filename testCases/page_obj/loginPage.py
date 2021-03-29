#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/10 17:26 
# @Author : wei.zhang
# @File : loginPage.py
# @Software: PyCharm

from basefactory.webdriveroperator import WebdriverOperator
from basefactory.browseroperator import BrowserOperator


class loginPage():
    def __init__(self):
        self.driver = None
        self.browser_opr = BrowserOperator()

    def open_url(self):
        """
        打开URL
        :return:
        """
        isOK, result = self.browser_opr.open_url(locator='http://qa-flowers.zhuihuazu.com/login')
        self.webdriver_opr = WebdriverOperator(result)

    def Wait_login_elements_visible(self):
        """
        等待登录元素出现
        :param type:
        :param locator:
        :param time:
        :return:
        """
        _isOK, _strLog = self.webdriver_opr.web_implicitly_wait(type='xpath',
                                                                locator='//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/img',
                                                                time=5)
        return _isOK, _strLog

    def Click_phone_number_login(self):
        """
        点击手机号登录
        :return:
        """
        _isOK, _strLog = self.webdriver_opr.element_click(type='xpath',
                                                          locator='//*[@id="root"]/div/div[2]/div[2]/div/div[2]/div/div[1]/div/img')
        return _isOK, _strLog

    def input_login_phone_number(self, phoneNumber):
        """
        输入登录手机号
        :param phoneNumber:
        :return:
        """
        _isOK, _strLog = self.webdriver_opr.element_input(type='xpath', locator='//*[@id="basic_mobile"]',
                                                          input=phoneNumber)
        return _isOK, _strLog

    def input_login_sms(self, sms):
        """
        输入验证码
        :param phoneNumber:
        :return:
        """
        _isOK, _strLog = self.webdriver_opr.element_input(type='xpath', locator='//*[@id="basic_verifyCode"]',
                                                          input=sms)
        return _isOK, _strLog

    def Click_login(self):
        """
        点击手机号登录
        :return:
        """
        _isOK, _strLog = self.webdriver_opr.element_click(type='xpath',
                                                          locator='//*[@id="basic"]/div[3]/div/div/div/button')
        return _isOK, _strLog

    def get_home_txt(self):
        _isOK, _strLog = self.webdriver_opr.get_text(type='xpath',
                                                     locator='//*[@id="root"]/div/section/aside/div/div/ul/li[1]/div[1]/span')
        return _isOK, _strLog
