# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 13:47
# @Author   : Gritli

# 登录失败
login_error = [
    {"username": "", "password": "", "expected": "请输入手机号"},
    {"username": "12", "password": "", "expected": "请输入正确的手机号"},
]

# 登录成功
login_success = [
    {"username":"18684720553", "password": "python", "expected": "我的帐户[python]"}
]

#登录未授权
login_invalid = [
    {"username":"18684720553","password":"www","expected":"帐号或密码错误!"}
]

#投资金额不是10的整数倍
invest_not_10_times = [
    {"money":1,"expected":"请输入10的整数倍"}
]

#投标成功
invest_success = [
    {"money":100,"expected":"投标成功！"}
]