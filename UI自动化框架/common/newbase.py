from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from common.logger import log
"""
关键字基类二次封装以及功能完善
"""

class Webpage:
    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver =driver

    def get_url(self,url):
        self.driver.maximize_window()
        self.driver.get(url)
        log.info("打开网页：%s" % url)

    # 查找元素
    def locator(self, name, value):
        """
        name：定位方式，value：定位值
        """
        # element = WebDriverWait(self.driver,timeout=30,poll_frequency=0.5).until(EC.visibility_of_element_located)
        self.wait_elevisible(name, value)
        return self.driver.find_element(name, value)

    # 等待
    def wait_elevisible(self, name, value, timeout=30, poll_frequency=0.5):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located((name, value)))
        except Exception as e:
            print('等待超时')

    # 点击元素
    def click_left(self, name, value):
        """加入显性等待点击，单击鼠标左键点击"""
        ele = self.locator(name, value)
        ele.click()
        log.info = ('正在获取元素属性值{}{}并点击'.format(name, value))

    # 输入文本
    def input(self, name, value, text):
        """输入前先清空"""
        ele = self.locator(name, value)
        ele.clear()
        ele.send_keys(text)
        log.info = ('正在获取元素属性值{}{}并输入'.format(name, value))
    # 添加cookie
    def add_cookie(self,cookie):
        self.driver.add_cookie(cookie)

    # 刷新
    def web_refresh(self):
        self.driver.refresh()


    # 获取元素文本值
    def get_text(self,name,value):
        text=self.locator(name,value).text
        return text