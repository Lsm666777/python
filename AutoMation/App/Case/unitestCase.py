#s导入unittest框架
import unittest
import time

from Tools.selenium_mouse import selenium_mouse
#
from Tools.PythonHelpApi import PythonHelpApi
#调用浏览器相关类
from Tools.BrowserConfig import BrowserConfig
#导入selenium鼠标机制
from Tools.selenium_mouse import selenium_mouse

from Tools.Selenium_WebElement import Selenium_WebElement

#定义一个类模块测试用例类，并继承Testcase类管理用例
class PosCartFuntciontestCase(unittest.TestCase):
    #继承TestCase类中setUpClass方法
    @classmethod
    def setUpClass(self):
        #self.URL = 'http://localhost:7012/pos'
        self.URL = 'http:192.168.0.115:7090/cold'
        BrowserConfig().BrowserGetUrl(self.URL)
    @classmethod
    def tearDownClass(cls):

        # 真正结束清理代码段
        BrowserConfig().BrowserQuit()
    #继承TestCase类中的初始化方法
    def setUp(self):
        BrowserConfig().BrowserGetUrl(self.URL)
        #self.Url = 'test-lsm.51zhongzi.com:7010/pos'
        #BrowserConfig().GetUrl(URl)
        BrowserConfig().BrowserMax()
    def tearDown(self):
        BrowserConfig().BrowserQuit()

    def testPosCaed001(self):

        time.sleep(1)
        Selenium_WebElement().Element_id(PythonHelpApi().ReadExcelData("UserName1",1,2)).send_keys(13212345678)
        time.sleep(1)
        Selenium_WebElement().Element_id(PythonHelpApi().ReadExcelData("UserName1",2,2)).send_keys(123456)
        time.sleep(1)
        Selenium_WebElement().Element_Xpath(PythonHelpApi().ReadExcelData("UserName1",3,2)).click()
        #点击门店管理
        time.sleep(1)
        Selenium_WebElement().Element_Xpath(PythonHelpApi().ReadExcelData("UserName1",4,2)).click()
        time.sleep(1)
        Selenium_WebElement().Element_Xpath(PythonHelpApi().ReadExcelData("UserName1", 5, 2)).click()
        time.sleep(1)
        Selenium_WebElement().Element_Xpath(PythonHelpApi().ReadExcelData("UserName1", 6, 2)).click()
        #断言
        time.sleep(1)
        #a=Selenium_WebElement().Element_Xpath(PythonHelpApi().ReadExcelData("UserName1", 10, 2)).click()

        expValue = PythonHelpApi().ReadExcelData("UserName1",11,2)
        c = Selenium_WebElement().Element_Xpath(PythonHelpApi().ReadExcelData("UserName1",11,2))
        selenium_mouse().double_mouse(c)
        time.sleep(1)
        actValue = Selenium_WebElement().Element_Xpath(PythonHelpApi().ReadExcelData("UserName1",10,2)).text
        try:
            self.assertEqual(actValue, expValue)
        except Exception as err:
            assert False, \
                "预期结果为:%s,实际结果为:%s" % (expValue, actValue)

#主函数
if __name__ == '__main__':
        unittest.main()

