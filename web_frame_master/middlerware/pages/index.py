# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 13:32
# @Author   : Gritli

#登录成功页面
from selenium.webdriver.common.by import By

from common.basepage import BasePage
from middlerware.middlerware import Handler
from middlerware.pages.invest import InvestPage


class IndexPage(BasePage):
    title = "互联网金融平台"

    URL = Handler.yaml["host"] + "/Index.html"

    #获取用户信息
    user_locator = (By.XPATH,'//a[@href="/Member/index.html"]')
    #点击抢投标
    click_invest_locator = (By.CLASS_NAME,"btn-special")

    def get(self):
        self.driver.get(self.URL)
        return self

    def get_account_name(self):
        """获取用户名"""
        el = self.driver.find_element(*self.user_locator)
        return el.text

    def click_invest_btn(self):
        """点击抢投标"""
        self.driver.find_element(*self.click_invest_locator).click()
        return InvestPage(self.driver)