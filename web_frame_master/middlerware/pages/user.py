# -*- coding: utf-8 -*-
# @Time     : 2020/8/2 22:41
# @Author   : Gritli
from selenium.webdriver.common.by import By

from common.basepage import BasePage


class UserPage(BasePage):
    title = "个人中心"

    # 用户余额
    user_balance = (By.CLASS_NAME, "color_sub")

    def get_balance(self):
        """获取余额"""
        el = self.wait_element_visible(self.user_balance)
        return el.text[:-1]

