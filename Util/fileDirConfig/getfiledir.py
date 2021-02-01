#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/9/9 16:25 
# @Author : wei.zhang
# @File : getfiledir.py
# @Software: PyCharm
import os

CASEDIR = os.path.abspath(os.path.join(os.getcwd(), "../testCases"))
REPORTDIR = os.path.abspath(os.path.join(os.getcwd(), "../testResult"))
LOGDIR = os.path.abspath(os.path.join(os.getcwd(), "../testResult/Logs"))
SCREENCAPTUREDIR = os.path.abspath(os.path.join(os.getcwd(), "testResult/ScreenCapture"))
EXCUTEDATADIR = os.path.abspath(os.path.join(os.getcwd(), "../testCases/exeuteData"))
PAGEOBJDIR = os.path.abspath(os.path.join(os.getcwd(), "../testCases/pageObj"))
