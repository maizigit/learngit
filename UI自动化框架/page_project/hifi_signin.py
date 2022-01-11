from common.newbase import Webpage
from selenium import webdriver

class Sign(Webpage):
    sign_button_name = 'xpath'
    sign_button_value ='//*[@id="sign"]'
    # URL_sign = 'https://www.hifini.com/sg_sign.htm'

    def sign(self):
        self.get_url('https://www.hifini.com/sg_sign.htm')
        status = self.get_text(self.sign_button_name,self.sign_button_value)
        if status =='已签':
            print('今日已经签到，请勿重复操作！')
        else:
            self.click_left(self.sign_button_name,self.sign_button_value)
    def huahua(self):
        print('花花')

if __name__ == '__main__':

    driver = webdriver.Chrome()
    sg = Sign(driver)
    sg.sign()
