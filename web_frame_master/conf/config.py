# -*- coding: utf-8 -*-
# @Time     : 2020/7/12 9:41
# @Author   : Gritli

import os

#config存放所有路径
#获取当前路径


file_path = os.path.dirname(os.path.abspath(__file__))

#获取项目路径

project_path = os.path.dirname(file_path)

#excel测试数据路径

data_path = os.path.join(project_path,"data")

# 测试用例路径
case_path = os.path.join(project_path, 'cases')

# 测试报告路径
reports_path = os.path.join(project_path, "reports")

# LOG 数据路径
log_path = os.path.join(project_path, "logs")

#yaml数据路径
yaml_path = os.path.join(file_path,"config.yml")

#img路径
IMG_path = os.path.join(log_path,"img")

WAIT_TIME = 20
