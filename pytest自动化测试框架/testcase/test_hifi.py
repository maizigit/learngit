from common.base import Webbage
import pytest
from selenium import webdriver
import time

class TestCase:
    def test_001(self):
        # 打开浏览器
        d = Webbage()
        d.get_url('https://www.baidu.com/')
        d.input('id','kw','今日说法')
        time.sleep(5)




