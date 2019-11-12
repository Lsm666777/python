from Utils.GetAppiumIndex import getAppiumIndex
class shoppage(object):
    def __init__(self):
        self.driver = getAppiumIndex().driver
    #点击招揽图
    def picture(self):
        self.driver.find_element_by_id("com.example.nft.nftongapp:id/rl_photo").click()
    def addpicture(self):
        self.driver.find_element_by_id("com.example.nft.nftongapp:id/iv_photo").click()
    def tap(self):
        self.driver.tap([(550,1600)])