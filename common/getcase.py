#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/9 14:35 
# @Author : wei.zhang
# @File : getcase.py
# @Software: PyCharm
import os

import openpyxl


class ReadCase(object):
    def __init__(self):
        filedir = os.path.abspath(os.path.join(os.getcwd(), "../caseData/test.xlsx"))
        self.sw = openpyxl.load_workbook(filedir)

    def openxlsx(self, file):
        """
        打开文件
        :param dir:
        :return:
        """
        self.sw = openpyxl.load_workbook(file)

    def readallcase(self):
        """
        取所有sheet页
        :return:list,返回sheet页里的数据
        """
        sheet_list = []
        for sh in self.sw:
            if 'common' != sh.title.split('_')[0] and 'common' != sh.title.split('-')[0] and sh.title[0] != '#':
                isOK, result = self.readcase(sh)
                if isOK:
                    sheet_list.append(result)
        if sheet_list is None:
            return False, '用例集是空的，请检查用例'
        return True, sheet_list

    def readcase(self, sh):
        """
        组合sheet页的数据
        :param sh:
        :return: list,返回组合数据
        """
        if sh is None:
            print('sheet页为空')
        datas = list(sh.rows)
        if datas == []:
            return False, '用例[' + sh.title + ']里面是空的'
        title = [i.value for i in datas[0]]
        rows = []
        sh_dict = {}
        for i in datas[1:]:
            data = [v.value for v in i]
            row = dict(zip(title, data))
            try:
                if str(row['id'])[0] != '#':
                    row['sheet'] = sh.title
                    rows.append(row)
            except KeyError:
                raise e
                rows.append(row)
            sh_dict[sh.title] = rows
        return True, sh_dict

    def get_common_case(self, case_name):
        """
        得到公共用例
        :param case_name:
        :return:
        """
        try:
            sh = self.sw.get_sheet_by_name(case_name)
        except KeyError:
            return False, '未找到公共用例[' + case_name + '],请检查用例'
        except DeprecationWarning:
            pass
        return self.readcase(sh)
