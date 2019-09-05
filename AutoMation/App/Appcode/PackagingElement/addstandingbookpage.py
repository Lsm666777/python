
from Utils.GetAppiumIndex import getAppiumIndex
class addstandingbookpage(object):
    def __init__(self):
        self.driver = getAppiumIndex().driver
#返回按钮
    def retur(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/back')
#添加客户
    def linkman(self):
       self.driver.find_element_by_id('com.azhyun.saas.e_account:id/add_linkman')
#主菜单
    def menu(self):
        self.driver.find_element_by_id('menu')
#输入姓名
    def imporName(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/edt_name')
#输入身份证号
    def IDnumber(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/edt_card')
#输入联系地址
    def address(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/edt_address')
#输入客户电话
    def phone(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/edt_phone')
#下一步
    def next(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/btn_next')