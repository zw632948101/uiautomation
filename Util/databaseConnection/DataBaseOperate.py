#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
@Time: 2019/12/31 19:43
@Author: hengxin
"""


import pymysql
import datetime
import decimal
import json
from Util.log import log
from os import getenv
from Util.dataDecryption import decrypt


class DataBaseOperate(object):

    def operate(self, host, sql):
        connection_config = decrypt(getenv('INTERFACE_CIPHER'))
        host = decrypt(host)
        if connection_config.get(host, None) is None:
            log.error("IP域名错误")
            exit(0)

        user = connection_config.get(host).get('user')
        password = connection_config.get(host).get('password')
        port = connection_config.get(host).get('port')

        db = pymysql.connect(host=host,
                             port=port,
                             user=user,
                             passwd=password)
        con = db.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            # 此处新增 单次连接执行多条SQL的功能, 兼容书写时首尾多输入空格的情况
            sql_list = sql.strip().split(";")
            try:
                # 此处兼容以分号结尾的单句SQL仍返回一维列表
                sql_list.remove('')
            except ValueError as e:
                log.error(e)
                raise Exception("SQL请以分号 ; 结束")
            if len(sql_list) < 2:
                con.execute(sql)
                log.debug(sql)
                effect_row = con.rowcount
                if sql.lower().startswith('select'):
                    log.debug(sql)
                    # if effect_row != 1:
                    #     log.info(sql)
                    # else:
                    #     pass
                    log.debug("影响行数 %s" % effect_row)
                else:
                    pass
                results = con.fetchall()
                db.commit()
                # print(results)
                for result in results:
                    for fields in result:
                        if isinstance(result[fields], datetime.datetime):
                            result[fields] = str(result[fields].strftime('%Y-%m-%d %H:%M:%S'))
                        elif isinstance(result[fields], datetime.date):
                            result[fields] = str(result[fields].strftime('%Y-%m-%d'))
                        elif isinstance(result[fields], decimal.Decimal):
                            result[fields] = float(result[fields])
            else:
                results = []
                for sql in sql_list:
                    if sql != '':
                        con.execute(sql)
                        log.debug(sql)
                        effect_row = con.rowcount
                        if sql.lower().startswith('select'):
                            log.debug(sql)
                            # if effect_row != 1:
                            #     log.info(sql)
                            # else:
                            #     pass
                        else:
                            pass
                        log.debug("影响行数 %s" % effect_row)
                        results.append(con.fetchall())
                        db.commit()
                    else:
                        pass
                for result in results:
                    for r in result:
                        for fields in r:
                            if isinstance(r[fields], datetime.datetime):
                                r[fields] = str(r[fields].strftime('%Y-%m-%d %H:%M:%S'))
                            elif isinstance(r[fields], datetime.date):
                                r[fields] = str(r[fields].strftime('%Y-%m-%d'))
                            elif isinstance(r[fields], decimal.Decimal):
                                r[fields] = float(r[fields])
            con.close()
            # if sql.lower().startswith('select'):
            log.debug("\n" + json.dumps(results, ensure_ascii=False,
                                                  sort_keys=True, indent=2, separators=(',', ': ')))
            # else:
            #     pass
            return results
        except Exception as e:
            db.rollback()
            log.error(e)
            raise KeyError(e)
