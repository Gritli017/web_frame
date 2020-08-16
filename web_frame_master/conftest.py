"""固定文件名 conftest.py.

存储所有的测试夹具。fixture
"""
import pytest

from conf.config import WAIT_TIME
from data.login_data import login_success
from middlerware.pages.login import LoginPage


@pytest.fixture(scope="function")
def driver():
    """管理浏览器"""

    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(WAIT_TIME)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def login(driver):
    """登录"""
    user_info = login_success[0]
    LoginPage(driver).get().login_success(
        username=user_info["username"],
        password=user_info["password"])
    yield driver