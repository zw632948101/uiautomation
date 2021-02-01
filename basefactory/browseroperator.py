#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/25 11:29 
# @Author : wei.zhang
# @File : browseroperator.py
# @Software: PyCharm
import os
from selenium import webdriver
from Util.Config import config
from Util.log import log


class BrowserOperator(object):
    def __init__(self):
        BASEFACTORYDIR = os.path.dirname(os.path.abspath(__file__))
        self.driver_path = os.path.join(BASEFACTORYDIR, 'chromedriver')

    def open_url(self, **kwargs):
        """
        打开网页
        :param kwargs:
        :return:
        """
        try:
            url = kwargs['locator']
        except KeyError:
            return False, '没有URL参数'

        try:
            type = config.get('BROWSER')  # 从配置文件里取浏览器的类型
            if type == 'chrome':
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('disable-infobars')
                chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])
                self.driver = webdriver.Chrome(options=chrome_options,
                                               executable_path=self.driver_path)
                # self.driver = webdriver.Chrome(executable_path=self.driver_path)
                self.driver.maximize_window()
                self.driver.get(url)
            elif type == 'IE':
                log.info('IE 浏览器')
            else:
                log.info('火狐浏览器')
        except Exception as e:
            return False, e
        return True, self.driver

    def close_browser(self, **kwargs):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()
        return True, '关闭浏览器成功'
