#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/8 16:45 
# @Author : wei.zhang
# @File : test_login_case.py
# @Software: PyCharm
from .page_obj.loginPage import loginPage
from .excuteData.loginData import LoginData
from .commonCase.common_login import CommonLogin
from common.runLevel import RunLevel
from ddt import data, unpack, ddt
import unittest


@ddt
class pageCase(unittest.TestCase):
    pagefun = loginPage()

    def setUp(self) -> None:
        self.pagefun.open_url()
        self.cl = CommonLogin(self.pagefun)

    def tearDown(self) -> None:
        self.pagefun.browser_opr.close_browser()

    @data(LoginData.one_login_data())
    @unpack
    @unittest.skipIf(RunLevel.skip_case(2), "执行等级小于设定等级 3，跳过该用例执行")
    def test_input_login(self, phone, sms):
        """
        该用例测试用户登录，检查首页加载完成首页看板文案
        :param phone: 手机号
        :param sms: 验证码
        :return:
        """
        self.cl.input_login(phone, sms)
        _isOK, _strLog = self.pagefun.get_home_txt()
        self.assertEqual('首页看板', _strLog, _strLog)

    @data(*LoginData.login_data())
    @unpack
    @unittest.skipIf(RunLevel.skip_case(case_level=5), "执行等级小于设定等级 5，跳过该用例执行")
    def test_2(self, phone, sms):
        _isOK, _strLog = self.pagefun.Wait_login_elements_visible()
        _isOK, _strLog = self.pagefun.Click_phone_number_login()
        _isOK, _strLog = self.pagefun.input_login_phone_number(phoneNumber=phone)
        _isOK, _strLog = self.pagefun.input_login_sms(sms=sms)
        _isOK, _strLog = self.pagefun.Click_login()
        _isOK, _strLog = self.pagefun.get_home_txt()
        self.assertEqual('首页看板', _strLog, _strLog)


if __name__ == '__main__':
    unittest.main(verbosity=2)
