from appium import webdriver

from Utils.GetAppiumIndex import getAppiumIndex
class LogonPageIndex(object):

    def __init__(self):
        self.driver = getAppiumIndex().driver

#手机号
    def PhoneNumber(self):
        try:
            PhoneNumber = self.driver.find_element_by_id('com.azhyun.saas.e_account:id/et_phone').send_keys(17800000000)
        except Exception as err:
            assert False,\
            "输入手机号文本框元素未找到"
        return PhoneNumber
#验证码
    def verifycode(self):
        try:
            verifycode = self.driver.find_element_by_id('com.azhyun.saas.e_account:id/et_code').send_keys(111111)
        except Exception as err:
            assert False,\
                "输入验证码文本框元素未找到"
        return verifycode
#登陆
    def login(self):
        try:
            login = self.driver.find_element_by_id('com.azhyun.saas.e_account:id/btn_login').click()
        except Exception as err:
            assert False,\
                "登陆按钮元素未找到"
        return login
#注册
    def register(self):
        try:
            register = self.driver.find_element_by_id('com.azhyun.saas.e_account:id/btn_register')
        except Exception as err:
            assert False,\
                "注册按钮元素未找到"
        return register