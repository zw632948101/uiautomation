#! /usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time:2021/1/29 17:40
# @Author: wei.zhang
# @File : test_day.py
# @Software: PyCharm
from basefactory import Base
from pageObj.baiduLogin import LoginPage
import time


class TestDay(Base):
    def setup(self) -> None:
        isok, result = self.openweb.open_url('http://qa-flowers.zhuihuazu.com/login')
        self.loginpage = LoginPage(result)

    def test_login(self):
        _isOK, _strLog = self.loginpage.Wait_login_elements_visible()
        assert _isOK, True
        _isOK, _strLog = self.loginpage.Click_phone_number_login()
        time.sleep(10)
