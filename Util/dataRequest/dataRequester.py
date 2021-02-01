#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
import json
import mimetypes
from Util.Config import config
from Util.log import log
import urllib


# from .recordExecuteAPI import RecordExecuteAPI as rea


class Request(object):
    version = config.get('version')
    headers = {"Content-Type": "application/x-www-form-urlencoded",
               "Accept": "application/json",
               "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/68.0.3440.106 Safari/537.36",
               "_App-Version_": version,
               "_Device-Type_": "iOS",
               "region": "online",
               "Accept_Language": "zh"
               }
    api_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "Host": "qa-gateway.worldfarm.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"}

    @staticmethod
    def url_encode(string):
        cn = ''
        for ch in string.decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                cn += urllib.quote(ch.encode('utf-8'))
            else:
                cn += ch.encode('utf-8')
        return cn

    def post(self, url, data, headers=None, hosts=None):
        client = requests.session()
        if headers is None:
            headers = self.headers.copy()
        if url.find('mgr.agrrobot.com') > 0:
            headers['Authentication-Token'] = data.get('_tk_')
        response = client.post(url=url, data=data, headers=headers, cookies=None).content
        log.info('headers: %s' % headers)
        log.debug('\n\trequest: %s\n\tdata: %s\n\tresponse: %s' % (url, data, response.decode("utf-8")))
        try:
            response_json = json.loads(response)
            log.debug("\n" + json.dumps(response_json, ensure_ascii=False,
                                        sort_keys=True, indent=2, separators=(',', ': ')))
        except ValueError:
            log.debug(response)
        # rea().reload_data(host_name=hosts, url=url)
        client.close()
        return response.decode("utf-8")

    def get(self, url, hosts=None, params=None):
        client = requests.session()
        if url.find('/v2/api-docs'):
            headers = self.api_headers
        else:
            headers = self.headers
        response = client.get(url=url, headers=headers, params=params).content
        try:
            log.debug('\n\trequest: %s\n\tresponse: %s\n\t' % (url, response.decode("utf-8")))
            response_json = json.loads(response.decode("utf-8"))
            # log.debug("\n" + json.dumps(response_json, ensure_ascii=False,
            #                                       sort_keys=True, indent=2, separators=(',', ': ')))
            log.debug("\n" + json.dumps(response_json))
        except ValueError:
            log.debug(response)
        # rea().reload_data(host_name=hosts, url=url)
        client.close()
        return response.decode("utf-8")

    def post_file(self, url, file_path, data=None, hosts=None):
        file_name = file_path.split("/")[-1:][0]
        file_bin_data = open(file_path, 'rb')
        content_type = str(mimetypes.types_map.get("." + file_path.split(".")[-1:][0], None))
        files = {'file': (file_name, file_bin_data, content_type)}
        headers = self.headers.copy()
        headers.pop('Content-Type')
        if url.find('mgr.agrrobot.com') > 0:
            headers['Authentication-Token'] = data.get('_tk_')
        response = requests.post(url=url, data=data, files=files, headers=headers).content
        log.debug('\n\trequest: %s\n\tfile: %s\n\tresponse: %s' % (url, file_path, response.decode("utf-8")))
        try:
            response_json = json.loads(response)
            log.debug("\n" + json.dumps(response_json, ensure_ascii=False,
                                        sort_keys=True, indent=2, separators=(',', ': ')))
        except ValueError:
            log.debug(response)
        # rea().reload_data(host_name=hosts, url=url)
        return response.decode("utf-8")
