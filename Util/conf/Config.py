#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 2020/8/31 10:58 
# @Author : wei.zhang
# @File : Config.py
# @Software: PyCharm

import yaml
from os.path import abspath, dirname
from Util.log import log
from configparser import ConfigParser


def get_config(file_path=None):
    if file_path is None:
        file_path = dirname(abspath(__file__))
        file_path = file_path + '/config.yaml'

    with open(file_path, encoding='utf-8') as f:
        config = yaml.safe_load(f)
        if config.get('which_project') in config.keys():
            return config.get(config.get('which_project'))
        else:
            log.error('未选择项目配置!')
            exit(0)


def get_ini(file_path=None):
    if file_path is None:
        file_path = dirname(abspath(__file__))
        file_path = file_path + '/base.ini'
    cfg = ConfigParser()
    cfg.read(file_path, encoding='UTF-8')
    cfg.sections()
    return cfg
