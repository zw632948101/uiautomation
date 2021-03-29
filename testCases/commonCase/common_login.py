#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/12 16:56 
# @Author : wei.zhang
# @File : common_login.py
# @Software: PyCharm

class CommonLogin(object):
    def __init__(self, browser):
        self.browser = browser


    def input_login(self, phone, sms):
        """
        该用例测试用户登录，检查首页加载完成首页看板文案
        :param phone: 手机号
        :param sms: 验证码
        :return:
        """
        _isOK, _strLog = self.browser.Wait_login_elements_visible()
        _isOK, _strLog = self.browser.Click_phone_number_login()
        _isOK, _strLog = self.browser.input_login_phone_number(phoneNumber=phone)
        _isOK, _strLog = self.browser.input_login_sms(sms=sms)
        _isOK, _strLog = self.browser.Click_login()
