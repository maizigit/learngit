from common.base import Webbage

from selenium import webdriver
import time


# 打开浏览器
d = Webbage()
d.get_url('https://www.baidu.com/')
# d.input('id','kw','今日说法')
# time.sleep(5)
d.get_cookie('mycookies')


