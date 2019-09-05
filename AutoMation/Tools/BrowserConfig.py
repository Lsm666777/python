#导入Bebdriver类库
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
import time
#导入单例模式
from Tools.Common import singleton
@singleton
#定义浏览器类
class BrowserConfig():
    #初始化方法（为该类下所有的方法有提供特殊的服务）
    def __init__(self):
        #浏览器实例化（打开xxx浏览器）
        self.driver = webdriver.Chrome()
    #定义浏览器输入URl方法
    def GetUrl(self,inputUrl):
        self.driver.get(inputUrl)
        # 打开网页需时间加载，需添加隐式等待
        self.driver.implicitly_wait(3)

    # 定义浏览器返回方法
    def BrowserBack(self):
        self.driver.back()

    # 定义浏览器前进方法
    def BrowserGo(self):
        self.driver.forward()
    # 定义浏览器关闭当前页面方法
    def BrowserClose(self):
        self.driver.close()
     # 定义浏览器关闭浏览器方法
    def BrowserQuit(self):
        self.driver.quit()
    # 定义浏览器刷新方法
    def BrowserRefresh(self):
        self.driver.refresh()
    # 定义浏览器页面最大化方法
    def BrowserMax(self):
        self.driver.maximize_window()
    # 定义浏览器页面最小化方法
    def Browsermin(self):
        self.driver.minimize_window()
    def BrowserGetUrl(self,revUrl):
        #基于打开的浏览器，输入URL，因通用方法，域名不能写死，只能变量化
        self.driver.get(revUrl)
        #打开网页需时间加载，需添加隐式等待
        self.driver.implicitly_wait(3)

    #浏览器显示等待
    def WebDriverWait(self,time,param,param1):
        self.WebDriverWait(webdriver,time,0.5).until(EC.presence_of_element_located(By.ID,param)).send_keys(param1)



