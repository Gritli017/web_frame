# -*- coding: utf-8 -*-
# @Time     : 2020/7/24 22:53
# @Author   : Gritli



# 1， 完成登录的自动化测试用例编写
# 2， 通过py文件和 pytest  实现数据驱动
# 3， locator 分层
# 4， PO 页面的链式调用
import pytest
import datetime

ts = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
if __name__ == "__main__":
    pytest.main(["--alluredir=allureout".format(ts)])