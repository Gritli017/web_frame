# -*- coding: utf-8 -*-
# @Time     : 2020/7/12 11:25
# @Author   : Gritli

import yaml

def read_yaml(file):
    """读取yaml文件中的数据"""
    with open(file,encoding='utf8') as f:
        conf = yaml.load(f,Loader=yaml.SafeLoader)
    return conf

def write_yaml(file,data):
    """将数据写入yaml文件中"""
    with open(file,'w',encoding='utf8') as f:
        yaml.dump(data,f)
