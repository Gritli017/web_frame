# -*- coding: utf-8 -*-
# @Time     : 2020/7/12 11:15
# @Author   : Gritli

import os

from common import yaml_handler,logging_handler

from conf.config import yaml_path,log_path,data_path



#封装Handler，Handler中初始化logger、excel_path
class Handler:
    #获取yaml路径
    yaml = yaml_handler.read_yaml(yaml_path)
    # logger
    logger_config = yaml["logger"]
    logger = logging_handler.get_logger(
        name=logger_config["name"],
        file=os.path.join(log_path, logger_config["file"]),
        logger_level=logger_config["logger_level"],
        stream_level=logger_config["stream_level"],
        file_level=logger_config["file_level"]
    )

    #excel
    excel_config = yaml["excel"]
    excel_path = os.path.join(data_path,excel_config["file"])

if __name__ == "__main__":
    pass


