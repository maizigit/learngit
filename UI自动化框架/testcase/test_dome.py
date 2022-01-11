import allure

from common.newbase import Webpage
# from common.base import Key
import pytest
import time
from excel_driver import yaml_read
from page_project.hifi_login import HifiLogin
from page_project.hifi_signin import Sign
from selenium import webdriver


@ allure.feature('测试HiFi签到模块')
class TestCase:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.hl = HifiLogin(self.driver)
        self.sg = Sign(self.driver)

    def teardown(self):
        pass

    @allure.story('利用cookie实现登陆')
    def test_001(self):
        self.hl.cookie_login()

    @allure.story('实现签到')
    def test_002(self):
        self.sg.sign()


# class TestCase:
#     @pytest.fixture(scope='class')
#     def open_hifi(self):
#         self.driver = webdriver.Chrome()
#         self.hl = HifiLogin(self.driver)
#         self.sg = Sign(self.driver)
#
#     def test_001(self):
#         self.hl.cookie_login()
#
#     def test_002(self):
#         self.sg.sign()


if __name__ == '__main__':
    pytest.main(['-vs','test_dome.py'])