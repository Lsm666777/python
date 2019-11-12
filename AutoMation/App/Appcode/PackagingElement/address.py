
from Utils.GetAppiumIndex import getAppiumIndex
class customerpage(object):

    def __init__(self):
        self.driver = getAppiumIndex().driver
#返回
    def retur(self):
        try:
            retur = self.driver.find_element_by_id('com.azhyun.saas.e_account:id/back')
        except Exception as err:
            assert False, \
            "返回按钮元素未找到"
        return retur

#添加客户
    def add(self):
        try:
            add = self.driver.find_element_by_id('com.azhyun.saas.e_account:id/back')
        except Exception as err:
            assert False, \
                "添加客户按钮元素未找到"
        return add

#主菜单
    def menu(self):
        try:
            menu = self.driver.find_element_by_id('com.azhyun.saas.e_account:id/title_menu')
        except Exception as err:
            assert  False,"主菜单按钮元素未找到"
        return menu

#输入姓名
    def imporName(self):
        try:
            imporName = self.driver.find_element_by_id('com.azhyun.saas.e_account:id/edt_name')
        except Exception as err:
            assert False,"姓名输入框元素未找到"
        return imporName
#输入身份证号
    def IDnumber(self):
        IDnumber = elf.driver.find_element_by_id('com.azhyun.saas.e_account:id/edt_card')
        return IDnumber
#输入联系地址
    def address(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/edt_address')
#输入客户电话
    def phone(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/edt_phone')
#保存
    def save(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/btn')