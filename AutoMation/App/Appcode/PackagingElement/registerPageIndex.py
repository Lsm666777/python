#from appium import webdriver
from Utils.GetAppiumIndex import getAppiumIndex
class registerPageIndex(object):
    def __init__(self):
        self.driver = getAppiumIndex().driver

#门店名称
    def ShopName(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/deit_store_name')
#联系人
    def linkman(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/deit_register_name')
#手机号
    def PhoneNumber(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/deit_register_moble')
#选择所在区域
    def selectregion(self):
        self.driver.find_element_by_class_name('android.widget.ImageView')

#详细地址
    def detailsite(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/deit_register_address')
#营业执照
    def picture(self):
        self.driver.find_element_by_id('com.azhyun.saas.e_account:id/img_register_business')