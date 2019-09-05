from appium import webdriver
from Utils.GetAppiumIndex import getAppiumIndex

class customerpage(object):

    def __init__(self):
        self.driver = getAppiumIndex().driver
#返回
    def retur(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/back')
#添加客户
    def add(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/back')
#主菜单
    def menu(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/title_menu')
