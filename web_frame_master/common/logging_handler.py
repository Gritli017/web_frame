# -*- coding: utf-8 -*-
# @Time     : 2020/7/12 13:08
# @Author   : Gritli


# -*- coding: utf-8 -*-
# @Time     : 2020/6/7 19:59
# @Author   : Gritli

import logging
# 对 logging 日志处理进行封装。使用 2 种方法：
# 函数封装 def get_logger()
#创建一个日志收集器
def get_logger(
        name="Gritli",
        file=None,
        logger_level="DEBUG",
        stream_level="DEBUG",
        file_level="INFO",
        fmt='%(asctime)s--[%(filename)s-->line:%(lineno)d]--%(levelname)s:%(message)s',
):
    """获取到收集器"""
    logger = logging.getLogger(name)
    # 设置收集器的级别
    logger.setLevel(logger_level)

    # 输出管理器
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(stream_level)
    logger.addHandler(stream_handler)

    # 格式
    fmt = logging.Formatter(fmt)
    stream_handler.setFormatter(fmt)

    if file:
        file_handler = logging.FileHandler(file, encoding='utf8')
        file_handler.setLevel(file_level)
        logger.addHandler(file_handler)
        file_handler.setFormatter(fmt)
    return logger