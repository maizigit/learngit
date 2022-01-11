'''
加载cookie登陆
'''
import time
from selenium import webdriver

from common.newbase import Webpage
# 需要登录后才能访问的一个接口
# driver.get('https://www.hifini.com/sg_sign.htm')
#
# # 抓取登录后的cookies并添加进来
# c1 = {'name': 'bbs_sid', 'value': 'r6ucpj5beqth1j78fih6dvt6ng'}
# c2 = {'name': 'bbs_token',
#       'value': '9Ng1idNpuXyhw40A4CSAhTvgD0GipJyt723utaQ_2BqhhIEHjEnpwz_2B4AeF96bl7TAqfIQhXM4NUw01NeSawOHN_2Fl_2FyX5xKlRb'}
# driver.add_cookie(c1)
# driver.add_cookie(c2)
# time.sleep(3)
# driver.refresh()


class HifiLogin(Webpage):
   URL_login ='https://www.hifini.com/sg_sign.htm'
   c1 = {'name': 'bbs_sid', 'value': 'r6ucpj5beqth1j78fih6dvt6ng'}
   c2 = {'name': 'bbs_token',
       'value': '9Ng1idNpuXyhw40A4CSAhTvgD0GipJyt723utaQ_2BqhhIEHjEnpwz_2B4AeF96bl7TAqfIQhXM4NUw01NeSawOHN_2Fl_2FyX5xKlRb'}

   def cookie_login(self):
       self.get_url(self.URL_login)
       self.add_cookie(self.c1)
       self.add_cookie(self.c2)
       time.sleep(3)
       self.web_refresh()

if __name__ == '__main__':
    driver = webdriver.Chrome()
    hl = HifiLogin(driver)
    hl.cookie_login()

