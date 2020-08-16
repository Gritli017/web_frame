# -*- coding: utf-8 -*-
# @Time     : 2020/7/26 11:20
# @Author   : Gritli


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from common.basepage import BasePage
from middlerware.middlerware import Handler
from middlerware.pages.index import IndexPage


class LoginPage(BasePage):
    title = "欢迎登录"
    URL = Handler.yaml["host"] + "/Index/login.html"
    #登录按钮、用户名、密码错误信息定位
    login_btn_locator = (By.CLASS_NAME, "btn-special")
    username_locator = (By.NAME,"phone")
    password_locator = (By.NAME,"password")
    error_msg_locator = (By.CLASS_NAME,"form-error-info")
    invalid_msg_locator = (By.CLASS_NAME,"layui-layer-content")


    def get(self):
        """获取页面"""
        self.driver.get(self.URL)
        return self

    def login_fail(self,username,password):
        """登录失败用例"""
        self.send_username(username)
        self.send_password(password)
        self.click_login()
        return self

    def login_success(self,username,password):
        """登录成功用例"""
        self.send_username(username)
        self.send_password(password)
        self.click_login()
        return IndexPage(self.driver)

    def login_invalid(self,username,password):
        """登录未授权"""
        self.send_username(username)
        self.send_password(password)
        self.click_login()
        return self

    def send_username(self,username):
        """输入帐号"""
        self.driver.find_element(*self.username_locator).send_keys(username)
        return self

    def send_password(self,password):
        """输入密码"""
        self.driver.find_element(*self.password_locator).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(*self.login_btn_locator).click()

    def get_error_message(self):
        """获取登录不成功的错误信息"""
        return self.driver.find_element(*self.error_msg_locator).text

    def get_invalid_message(self):
        """获取登录未授权的错误信息"""
        #添加显示等待
        el = self.wait_element_visible(self.invalid_msg_locator)
        return el.text

