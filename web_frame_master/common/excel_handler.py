# -*- coding: utf-8 -*-
# @Time     : 2020/7/12 13:18
# @Author   : Gritli


import openpyxl
#用于读取excel数据

def read_data(path,name):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[name]
    #获取所有行并转换成列表
    rows = list(sheet.rows)
    #定义一个空列表接收字典
    data = []
    #定义一个列表接收所有的标题
    headers = []
    #循环输出第一行并追加到headeres列表中
    for title in rows[0]:
        headers.append(title.value)
    #获取剩下行的数据
    for row in rows[1:]:
    #定义一个空字典接收每一行的数据
        row_data_dic = {}
        #将每一行的数据转换成字典
        for index , cell_value in enumerate(row):
            row_data_dic[headers[index]] = cell_value.value
        #将字典放入最外层的列表
        data.append(row_data_dic)
    return data