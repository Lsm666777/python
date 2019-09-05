
from Utils.GetAppiumIndex import getAppiumIndex
class loginpage(object):
    def __init__(self):
     self.driver = getAppiumIndex().driver
    def account(self):
        self.driver.find_element_by_id('com.example.nft.nftongapp:id/tv_zh_content').send_keys(13812345672)
    def password(self):
        self.driver.find_element_by_id("com.example.nft.nftongapp:id/tv_mm_content").send_keys(111111)
        #点击登录按钮
    def login(self):
        self.driver.find_element_by_id("com.example.nft.nftongapp:id/rl_login").click()
        #点击添加账号
    def addaccount(self):
        self.driver.find_element_by_id("com.example.nft.nftongapp:id/tv_zczh").click()
        #点击忘记密码
    def forgetpasswrod(self):
        self.driver.find_element_by_id("com.example.nft.nftongapp:id/tv_wjmm").click()

        