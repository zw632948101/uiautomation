#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/31 14:35 
# @Author : wei.zhang
# @File : factory.py
# @Software: PyCharm


from Util.conf import ini
from common.getcase import ReadCase
from basefactory.browseroperator import BrowserOperator
from basefactory.webdriveroperator import WebdriverOperator


class Factory(object):

    def __init__(self):
        self.con = ini
        self.con_fun = dict(self.con.items('Function'))

        """
        浏览器操作对象
        """
        self.browser_opr = BrowserOperator()
        """
        网页操作对象
        """
        self.webdriver_opr = None

        # 初始化公共用例

    def init_common_case(self, cases):
        """
        :param kwargs:
        :return:
        """
        cases_len = len(cases)
        index = 0
        for case in cases:
            if case['keyword'] == '调用用例':
                xlsx = ReadCase()
                try:
                    case_name = case['locator']
                except KeyError:
                    return False, '调用用例没提供用例名，请检查用例'
                # 取公共用例
                isOK, result = xlsx.get_common_case(case_name)
                if isOK and type([]) == type(result):
                    # 递归检查公共用例里是否存在调用用例
                    isOK, result_1 = self.init_common_case(result)
                elif not isOK:
                    return isOK, result
                list_rows = result[case_name]
                cases[index: index + 1] = list_rows  # 将公共用例插入到执行用例中去
            index += 1
        if cases_len == index:
            return False, ''
        return True, cases

        # 初始化执行用例

    def init_execute_case(self):
        print("----------初始化用例----------")
        xlsx = ReadCase()
        isOK, result = xlsx.readallcase()
        if not isOK:
            print(result)
            print("----------结束执行----------")
            exit()
        all_cases = result
        excu_cases = []
        for cases_dict in all_cases:
            for key, cases in cases_dict.items():
                isOK, result = self.init_common_case(cases)  # 将取的执行用例，去初始化一下公共用例
                if isOK:
                    cases_dict[key] = result
                else:
                    cases_dict[key] = cases
                excu_cases.append(cases_dict)
                print("----------初始化用例完成----------")
        return excu_cases

    def init_webdriver_opr(self, driver):
        self.webdriver_opr = WebdriverOperator(driver)

    def get_base_function(self, function_name):
        try:
            function = getattr(self.browser_opr, function_name)
        except Exception:
            try:
                function = getattr(self.webdriver_opr, function_name)
            except Exception:
                return False, '未找到注册方法[' + function_name + ']所对应的执行函数，请检查配置文件'
        return True, function

    def execute_keyword(self, **kwargs):
        """
        工厂函数，用例执行方法的入口
        :param kwargs:
        :return:
        """
        try:
            keyword = kwargs['keyword']
            if keyword is None:
                return False, '没有keyword，请检查用例'
        except KeyError:
            return False, '没有keyword，请检查用例'

        _isbrowser = False

        try:
            function_name = self.con_fun[keyword]
        except KeyError:
            return False, '方法Key[' + keyword + ']未注册，请检查用例'

        # 获取基础类方法
        isOK, result = self.get_base_function(function_name)
        if isOK:
            function = result
        else:
            return isOK, result

        # 执行基础方法，如打网点页、点击、定位、隐式等待 等
        isOK, result = function(**kwargs)

        # 如果是打开网页，唯一一次初始化浏览器，需要将webdriver传参给另一个基础类，方便他操控元素
        if '打开网页' == keyword and isOK:
            url = kwargs['locator']
            self.init_webdriver_opr(result)
            return isOK, '网页[' + url + ']打开成功'

        return isOK, result

