from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from common.logger import log


# 创建浏览器对象

# def open_browser(txt):
#     # if txt == 'Chrome':
#     #     driver = webdriver.Chrome()
#     # elif txt == 'Ie':
#     #     driver = webdriver.Ie()
#     # else:
#     #     driver = webdriver.Firefox()
#     try:
#         driver = getattr(webdriver, txt)()
#     except Exception as e:
#         print(e)
#         driver = webdriver.Chrome()
#
#     return driver
def open_browser(text):
    # 基于反射机制简化代码
    global driver
    try:
        driver = getattr(webdriver, text)()

    except Exception as e:
        print(e)
        driver = webdriver.Chrome()
    return driver


class Key:
    # 创建临时的driver对象
    # driver = webdriver.Chrome()
    # 初始化driver
    def __init__(self, text):
        log.info =('初始化driver{}'.format(text))
        self.driver = open_browser(text)
        self.driver.maximize_window()

    # 访问url
    def open(self, text):
        log.info =('正在打开{}url'.format(text))
        self.driver.get(text)

    # 截图
    # def capture(self,model_name='error'):
    #     recordpath = record_dir + "/{}_{}.png".format(model_name,
    #                                                   time.strftime("%Y-%m-%d-""%H-%M-%S", time.localtime()))
    #     try:
    #         self.driver.get_screenshot_as_file(recordpath)
    #     except Exception as e:
    #         log.error("截图失败：{}".format(e))




    # 查找元素
    def locator(self, name, value):
        """
        name：定位方式，value：定位值
        """
        # element = WebDriverWait(self.driver,timeout=30,poll_frequency=0.5).until(EC.visibility_of_element_located)
        self.wait_elevisible(name,value)
        return self.driver.find_element(name, value)

    # 等待
    def wait_elevisible(self,name,value,timeout=30, poll_frequency=0.5):
        try:
             WebDriverWait(self.driver,timeout, poll_frequency).until(EC.visibility_of_element_located((name,value)))
        except Exception as e:
            print('等待超时')

    # 点击元素
    def click_left(self, name, value):
        """加入显性等待点击，单击鼠标左键点击"""
        log.info =('正在获取元素属性值{}{}并点击'.format(name,value))
        ele = self.locator(name, value)
        ele.click()

    # 输入文本
    def input(self, name, value, text):
        """输入前先清空"""
        log.info= ('正在获取元素属性值{}{}并输入'.format(name,value))
        ele = self.locator(name, value)
        ele.clear()
        ele.send_keys(text)

    # 获取文本值
    def get_eletext(self,name,value):
        """获取当前的text"""
        _text = self.locator(name,value).text
        return _text

    # 刷新
    def refresh(self):
        """刷新页面F5"""
        self.driver.refresh()
        self.driver.implicitly_wait(30)

    # 关闭浏览器

    def quit(self):
        self.driver.quit()
