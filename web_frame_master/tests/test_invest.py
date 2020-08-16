
"""投资"""
import time

from conftest import login
from data.login_data import invest_not_10_times, invest_success
import pytest

from middlerware.middlerware import Handler
from middlerware.pages.index import IndexPage



@pytest.mark.parametrize("data_info",invest_not_10_times)
def test_invest_not_10_times(login,data_info):
    """投资不是 10 的整数倍。
    测试步骤：
        1， 前置条件：登录（）
            - 有钱
            - 有标可以投
            可以通过接口，可以通过修改数据库，可以手工充值，可以手工加标。
            - 每次你在执行之前都自动充值或者加一次标
            - 一次性满足条件

        2， 首页：点击抢投标
        3， 投标详情页：输入投标金额
        4， 投标详情页：获取结果
    """
    driver = login
    #time.sleep(2)
    actual = IndexPage(driver).click_invest_btn().input_money(money=data_info["money"]).get_error_msg()
    #将预期结果跟实际结果记录在日志中
    Handler.logger.info(actual)
    Handler.logger.info(data_info["expected"])
    assert actual == data_info["expected"]

@pytest.mark.parametrize("data_info",invest_success)
def test_invest_success(login,data_info):
    """投标成功"""
    driver = login
    invest_page = IndexPage(driver).click_invest_btn()
    #获取投标前的金额
    before_money = invest_page.get_money()
    #获取实际结果
    success_msg = invest_page.input_money(data_info["money"]).click_invest_btn().get_success_msg()
    #断言投资成功后的提示语
    assert  data_info["expected"] in success_msg
    after_money = invest_page.click_active_btn().get_balance()
    from decimal import Decimal
    #断言投资成功后的金额
    amount = Decimal(str(data_info["money"]))
    assert Decimal(before_money) - Decimal(str(data_info["money"])) == Decimal(after_money)
