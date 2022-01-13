"""
selenium 关键字的二次封装
"""
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common.syslog import log

class Webbage:

    def __init__(self):
        self.driver = webdriver.Chrome()

    # 打开某url
    def get_url(self,url):
        try:
            self.driver.maximize_window()
            self.driver.get(url)
            self.driver.implicitly_wait(time_to_wait=30)
            log().info("打开网页：%s" % url)
        except Exception as e:
            log().info('打开网页失败：%s' % url)

    # 查找元素
    def locator(self, name, value):
        """
        name：定位方式，value：定位值
        """
        # element = WebDriverWait(self.driver,timeout=30,poll_frequency=0.5).until(EC.visibility_of_element_located)
        self.wait_elevisible(name, value)
        return self.driver.find_element(name, value)
    # 显性等待
    def wait_elevisible(self, name, value, timeout=30, poll_frequency=0.5):
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.visibility_of_element_located((name, value)))
        except Exception as e:
            log().info('等待超时')

    # 左键点击
    def click_left(self, name, value):
        """加入显性等待点击，单击鼠标左键点击"""
        try:
            ele = self.locator(name, value)
            ele.click()
            log().info = ('正在获取元素属性值{}{}并点击'.format(name, value))
        except  Exception as e:
            log().info('点击元素{}{}失败,请检查定位'.format(name,value))

    # 输入文本
    def input(self, name, value, text):
        """输入前先清空"""
        ele = self.locator(name, value)
        ele.clear()
        ele.send_keys(text)
        log().info("输入文本：{}".format(text))

    # 添加cookie
    def add_cookie(self,cookie):
        self.driver.add_cookie(cookie)

    # 获取cookie
    def get_cookies(self):
        self.driver.get_cookies()



