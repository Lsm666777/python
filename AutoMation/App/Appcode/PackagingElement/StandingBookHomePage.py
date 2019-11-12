from appium import webdriver

from Utils.GetAppiumIndex import getAppiumIndex

class HomePageIndex(object):

    def __init__(self):
        self.driver = getAppiumIndex().driver
#添加台账
    def addstandingbook(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/add_layout')
#客户管理
    def customer(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/customer_layout')
#应收账款
    def receivables(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/receivable_layout')
#历史台账
    def historystandingbook(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/history_layout')
#商品管理
    def shopmanage(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/goods_layout')
#售后服务

#设置
    def settings(self):
        try:
            settings = self.driver.find_element_by_id('com.azhyun.saas.e_account:id/main_shezhi')
        except Exception as err:
            assert False,\
                "输入验证码文本框元素未找到"
        return settings