#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/31 11:30 
# @Author : wei.zhang
# @File : webdriveroperator.py
# @Software: PyCharm

import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from Util.conf import config
from Util.log import log
from Util.fileDirConfig.getfiledir import SCREENCAPTUREDIR


class WebdriverOperator(object):

    def __init__(self, driver: Chrome = None):
        self.driver = driver
        self.timeout = config.get('TIMEOUT')
        self.poll_frequency = config.get('POLL_FREQUENCY')
        self.deriver_type = 'chrome'

    def get_screenshot_as_file(self):
        """
        截屏保存
        :return:返回路径
        """
        pic_name = str.split(str(time.time()), '.')[0] + str.split(str(time.time()), '.')[
            1] + '.png'
        screent_path = SCREENCAPTUREDIR + '/' + pic_name
        self.driver.get_screenshot_as_file(screent_path)
        return screent_path

    def gotosleep(self, **kwargs):
        log.warning('线程等待：3秒')
        time.sleep(3)
        return True, '等待成功'

    def web_implicitly_wait(self, **kwargs):
        """
        隐式等待
        :return:
        type_  存时间
        """
        try:
            s = kwargs['time']
        except KeyError:
            s = 10
        log.info('隐式等待 元素加载完成')
        try:
            self.driver.implicitly_wait(s)
        except NoSuchElementException:
            return False, '隐式等待 页面元素未加载完成'
        return True, '隐式等待 元素加载完成'

    def __find_element(self, locator: tuple):
        """
        :param tuple locator:(By.xxxxx, locator)定位参数
        :return:返回元素对象
        """
        try:
            elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                lambda x: x.find_element(*locator))
        except NoSuchElementException:
            log('元素[' + locator[1] + ']等待出现超时')
            return False, '元素[' + locator[1] + ']等待出现超时'
        return True, elem

    def __find_elements(self, locator: tuple):
        """
        传入定位器参数locator=(By.XX,"value")
        :param tuple locator:
        :return: 返回元素对象列表
        """
        try:
            elem = WebDriverWait(self.driver, self.timeout, self.poll_frequency).until(
                lambda x: x.find_elements(*locator))
            return True, elem
        except NoSuchElementException:
            log('元素[' + locator[1] + ']等待出现超时')
            return False, '元素[' + locator[1] + ']等待出现超时'

    def web_element_wait(self, **kwargs):
        """
        等待元素可见
        :return:
        """
        try:
            type_ = kwargs['type']
            locator = kwargs['locator']
        except KeyError:
            return False, '未传需要等待元素的定位参数'
        if type_ == 'id':
            isok, logs = self.__find_element((By.ID, locator))
        elif type_ == 'name':
            isok, logs = self.__find_element((By.NAME, locator))
        elif type_ == 'class':
            isok, logs = self.__find_element((By.CLASS_NAME, locator))
        elif type_ == 'xpath':
            isok, logs = self.__find_element((By.XPATH, locator))
        elif type_ == 'css':
            isok, logs = self.__find_element((By.CSS_SELECTOR, locator))
        else:
            return False, '不能识别元素类型[' + type_ + ']'
        if isok:
            return True, '元素[' + locator + ']等待出现成功'
        else:
            return False, '元素[' + locator[1] + ']等待出现超时'

    def find_element(self, type_, locator):
        """
        定位元素
        :param type_: 定位类型
        :param locator: 元素
        :return: 返回定位元素
        """
        type_ = str.lower(type_)
        try:
            if type_ == 'id':
                isok, elem = self.__find_element((By.ID, locator))
            elif type_ == 'name':
                isok, elem = self.__find_element((By.NAME, locator))
            elif type_ == 'class':
                isok, elem = self.__find_element((By.CLASS_NAME, locator))
            elif type_ == 'xpath':
                isok, elem = self.__find_element((By.XPATH, locator))
            elif type_ == 'css':
                isok, elem = self.__find_element((By.CSS_SELECTOR, locator))
            else:
                return False, '不能识别元素类型:[' + type_ + ']'
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            return False, '获取[' + type_ + ']元素[' + locator + ']失败,已截图[' + screenshot_path + '].'
        return isok, elem

    def find_elements(self, type_, locator, index=0):
        """
        定位元素
        :param type_: 定位类型
        :param locator: 元素
        :return: 返回元素列表
        """
        try:
            if type_ == 'id':
                isok, elem = self.__find_elements((By.ID, locator))
            elif type_ == 'name':
                isok, elem = self.__find_elements((By.NAME, locator))
            elif type_ == 'class':
                isok, elem = self.__find_elements((By.CLASS_NAME, locator))
            elif type_ == 'xpath':
                isok, elem = self.__find_elements((By.XPATH, locator))
            elif type_ == 'css':
                isok, elem = self.__find_elements((By.CSS_SELECTOR, locator))
            else:
                return False, '不能识别元素类型:[' + type_ + ']'
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            return False, '获取[' + type_ + ']元素[' + locator + ']失败,已截图[' + screenshot_path + '].'
        return isok, elem[index]

    def element_click(self, **kwargs):
        """
        点击
        :param kwargs:
        :return:
        """
        try:
            type_ = kwargs['type']
            locator = kwargs['locator']
            index = kwargs.get('index') if kwargs.get('index') else 0
        except KeyError:
            return False, '缺少传参'
        _isOK, _strLOG = self.find_elements(type_, locator, index)
        if not _isOK:  # 元素没找到，返回失败结果
            return _isOK, _strLOG
        elem = _strLOG
        try:
            elem.click()
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            return False, '元素[' + locator + ']点击失败,已截图[' + screenshot_path + '].'
        return True, '元素[' + locator + ']点击成功'

    def element_input(self, **kwargs):
        """
        输入
        :param kwargs:
        :return:
        """
        try:
            type_ = kwargs['type']
            locator = kwargs['locator']
            text = str(kwargs['input'])
            index = kwargs.get('index') if kwargs.get('index') else 0
        except KeyError:
            return False, '缺少传参'
        _isOK, _strLOG = self.find_elements(type_, locator, index)
        if not _isOK:  # 元素没找到，返回失败结果
            return _isOK, _strLOG
        elem = _strLOG
        try:
            elem.send_keys(text)
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            return False, '元素[' + locator + ']输入[' + text + ']失败,已截图[' + screenshot_path + '].'
        return True, '元素[' + locator + ']输入[' + text + ']成功'

    def get_text(self, **kwargs):
        """
        获得元素文本
        :param type_: 定位类型
        :param locator: 元素
        :return: 元素文本值
        """
        try:
            type_ = kwargs['type']
            locator = kwargs['locator']
            index = kwargs.get('index') if kwargs.get('index') else 0
        except KeyError:
            return False, '缺少传参'
        _isOK, elem = self.find_elements(type_, locator, index)
        if _isOK:
            elem = elem.text
        return _isOK, elem
