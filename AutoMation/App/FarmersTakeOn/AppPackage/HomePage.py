from Utils.GetAppiumIndex import getAppiumIndex
class homepage(object):
    def __init__(self):
        self.driver = getAppiumIndex().driver
    def setting(self):
        self.driver.find_element_by_id("com.example.nft.nftongapp:id/iv_setting").click()
    def inform(self):
        self.driver.find_element_by_id("com.example.nft.nftongapp:id/iv_alert").click()
    #累计金额
    def summoney(self):
        summoney = self.driver.find_element_by_id("com.example.nft.nftongapp:id/tv_sr").text
        print(str(summoney))
    #可用金额
    def usablemoney(self):
        usablemoney = self.driver.find_element_by_id("com.example.nft.nftongapp:id/tv_kyye_value").text
        print(str(usablemoney))
    #代发货
    def DelayShipments(self):
        DelayShipments = self.driver.find_element_by_id("selfcom.example.nft.nftongapp: id / tv_dfh_value").text
        print(str(DelayShipments))
    #今日下单
    def TodayOrder(self):
        TodayOrder = self.driver.find_element_by_id("com.example.nft.nftongapp: id / tv_jrxd_value").text
        print(str(TodayOrder))
    def Shop(self):
        self.driver.find_element_by_id("com.example.nft.nftongapp:id/iv_dpgl").click()


