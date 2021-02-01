#! /usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time: 2020 2020/2/26 15:19
__author__: wei.zhang

"""
import yaml
import os


class RecordExecuteAPI(object):
    def analysis_yaml(self, filename: str):
        """
        获取配置
        :return: 字典
        """
        try:
            config = open(filename, 'r').read()
        except FileNotFoundError:
            config = open(filename, 'w')
            config.close()
            config = open(filename, 'r').read()
        yaml_config = yaml.safe_load(config)
        return yaml_config

    def reload_data(self, host_name: str, url: str):
        """
        接受传参写入配置文件
        :param host_name:
        :param url:
        :return:
        """
        if host_name:
            hosts = host_name.split('-')[-1]
            uri = url.replace(host_name, '')
            file_path = os.path.dirname(__file__)
            filename = file_path + "/Attachment/ExecuteAPI/recordExecute" + hosts.capitalize() + "API.yaml"
            ydd = self.analysis_yaml(filename)
            if ydd:
                try:
                    ydd['uri'].append(uri)
                    uri_list = set(ydd['uri'])
                    ydd['uri'] = list(uri_list)

                except AttributeError:
                    ydd['uri'] = [uri]
                fw = open(filename, 'w', encoding='utf-8')
                yaml.dump(ydd, fw)
            else:
                with open(filename, 'w') as f:
                    f.write('uri: -%s' % uri)
