# -*- coding: utf-8 -*-
# @Time     : 2020/7/12 11:52
# @Author   : Gritli

import pymysql
from pymysql.cursors import DictCursor
class MysqlHandler():

    def __init__(self,host=None,port=3306,user=None,password=None,charset="utf8",cursorclass=DictCursor):

        self.conn = pymysql.connect(
            host=host,port=port,user=user,password=password,charset=charset,cursorclass=cursorclass)

        self.cursor = self.conn.cursor()
    def query(self,sql,one=True):
        self.conn.commit()
        self.cursor.execute(sql)
        if one:
            return self.cursor.fetchone()
        return self.cursor.fetchall()
    def close(self):
        self.cursor.close()
        self.conn.close()
