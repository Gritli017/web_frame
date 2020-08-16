# -*- coding: utf-8 -*-
# @Time     : 2020/7/12 17:03
# @Author   : Gritli

import requests
class RequestHandler:

    def __init__(self):
        pass

    def visit(
        url,
        method="get",
        params = None,
        data = None,
        json = None,
        **kwargs
    ):
        """访问接口，调用requests方法，传递URL，请求方式
        返回字典  res.json(）
        """
        res = requests.request(
            method,
            url,
            params = params,
            data = data,
            json = json,
            **kwargs
        )
        try:
            return res.json()
        except Exception as e:
            print(file="requests_logs.txt").error("返回的数据不是json格式{}".format(e))
            return None