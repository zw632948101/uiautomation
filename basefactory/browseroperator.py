#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/25 11:29 
# @Author : wei.zhang
# @File : browseroperator.py
# @Software: PyCharm
import os
from selenium import webdriver
from Util.conf import config
from Util.log import log
from Util import BASEFACTORYDIR


class BrowserOperator(object):
    def __init__(self):
        import platform
        system = platform.system()
        if system == 'Windows':
            find_util = 'chromedriver.exe'
        else:
            find_util = 'chromedriver'
        self.driver_path = os.path.join(BASEFACTORYDIR, find_util)

    def open_url(self, **kwargs):
        """
        打开网页
        :param kwargs:
        :return:
        """

        def __options(options):
            # 禁用浏览器正在被自动化程序控制的提示
            options.add_argument('--disable-infobars')
            # 浏览器不提供可视化页面
            if not config.get('HEADLESS'):
                options.add_argument('--headless')
            if config.get('DEBUG_MODE') == 'debugger':
                log.info(f'本地调试：{config.get("DEBUGGER_ADDERESS")},为空时不复用浏览器')
                options.debugger_address = config.get('DEBUGGER_ADDERESS')
            # 屏蔽自动化受控提示 && 开发者提示
            options.add_experimental_option("excludeSwitches", ['enable-automation'])
            # 禁用浏览器正在被自动化程序控制的提示
            options.add_experimental_option("useAutomationExtension", False)
            # 屏蔽'保存密码'提示框
            prefs = {}
            prefs["credentials_enable_service"] = False
            prefs["profile.password_manager_enabled"] = False
            options.add_experimental_option('prefs', prefs)
            """
            其他设置参数请参考以下链接
            https://peter.sh/experiments/chromium-command-line-switches/
            """
            return options

        try:
            url = kwargs['locator']
        except KeyError:
            log.error('kwargs没有URL参数:locator')
            return False, '没有URL参数'
        try:
            type = config.get('BROWSER')  # 从配置文件里取浏览器的类型
            if type == 'Chrome':
                log.info("选择使用Chrome浏览器")
                chrome_options = webdriver.ChromeOptions()
                chrome_options = __options(options=chrome_options)
                self.driver = webdriver.Chrome(options=chrome_options,
                                               executable_path=self.driver_path)
            elif type == 'IE':
                log.info('选择使用 IE 浏览器')
                ie_options = webdriver.IeOptions()
                ie_options = __options(options=ie_options)
                self.driver = webdriver.Ie(options=ie_options, executable_path=self.driver_path)
            elif type == 'Edge':
                log.info('选择使用 Edge 浏览器')
                self.driver = webdriver.Edge(executable_path=self.driver_path)
            elif type == 'Firfox':
                log.info('选择使用火狐浏览器')
                firfox_options = webdriver.FirefoxOptions()
                firfox_options = __options(options=firfox_options)
                self.driver = webdriver.Firefox(options=firfox_options,
                                                executable_path=self.driver_path)
            self.driver.maximize_window()
            self.driver.get(url)
            if config.get('DEBUG_MODE') == 'cookies':
                log.info('使用cookies测试')
                for cookie in config.get('COOKIES'):
                    if 'expiry' in cookie.keys():
                        cookie.pop('expiry')
                    self.driver.add_cookie(cookie)
                self.driver.refresh()
        except Exception as e:
            log.error(e.msg)
            return False, e
        return True, self.driver

    def close_browser(self, **kwargs):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()
        log.info('关闭浏览器成功')
        return True, '关闭浏览器成功'
