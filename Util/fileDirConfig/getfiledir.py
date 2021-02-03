#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/9 16:25 
# @Author : wei.zhang
# @File : getfiledir.py
# @Software: PyCharm
import os

# 测试用例路径
CASEDIR = os.path.abspath(os.path.join(os.getcwd(), "../testCases"))
# 测试报告路径
REPORTDIR = os.path.abspath(os.path.join(os.getcwd(), "../testResult"))
# log日志存放路径
LOGDIR = os.path.abspath(os.path.join(os.getcwd(), "../testResult/Logs"))
# 截图存放路径
SCREENCAPTUREDIR = os.path.abspath(os.path.join(os.getcwd(), "testResult/ScreenCapture"))
# 测试执行数据存放路径
EXCUTEDATADIR = os.path.abspath(os.path.join(os.getcwd(), "../testCases/exeuteData"))
# PO界面封装路径
PAGEOBJDIR = os.path.abspath(os.path.join(os.getcwd(), "../testCases/pageObj"))
# webdriver驱动程序存放路径
BASEFACTORYDIR = os.path.abspath(os.path.join(os.getcwd(), "../basefactory/webdriverapp"))
