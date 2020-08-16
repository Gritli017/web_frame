
"""登录功能"""


import pytest

from selenium import webdriver
from data.login_data import login_error,login_success, login_invalid
from conf.config import WAIT_TIME
from middlerware.middlerware import Handler
from middlerware.pages.login import LoginPage


class TestLogin():
    """登录功能的测试类"""
    Handler.logger.info("测试一下日志")
    @pytest.mark.error_test
    @pytest.mark.parametrize("data_info", login_error)
    def test_login_error(self,data_info,driver):
        # 初始化页面
        login_page = LoginPage(driver)
        #测试步骤
        actual = login_page.get().login_fail(
            username=data_info["username"],
            password=data_info["password"]
        ).get_error_message()
        #断言
        try:
            assert actual == data_info["expected"]
        except AssertionError as e:
            Handler.logger.error("测试用例不通过")
            raise e
    @pytest.mark.success
    @pytest.mark.parametrize("data_info",login_success)
    def test_login_success(self,data_info, driver):
        """登录成功用例"""
        login_page = LoginPage(driver)
        #测试步骤
        actual = login_page.get().login_success(
            username=data_info["username"],
            password=data_info["password"]
        ).get_account_name()

        try:
            assert actual == data_info["expected"]
        except AssertionError as e:
            Handler.logger.error("测试用例不通过")
            raise e
    @pytest.mark.invalid
    @pytest.mark.parametrize("data_info",login_invalid)
    def test_login_invalid(self,data_info,driver):
        """登录未授权"""
        #初始化页面
        login_page = LoginPage(driver)
        #测试步骤
        actual = login_page.get().login_invalid(
            username = data_info["username"],
            password = data_info["password"]
        ).get_invalid_message()
        try:
            assert actual == data_info["expected"]
        except AssertionError as e:
            Handler.logger.error("测试用例不通过")
            raise e







