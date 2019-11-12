#导入 unittest框架和时间类库
import unittest,time
#导入浏览器相关类（导入后具体业务场景使用该类下的属性或方法）
from Tools.BrowserConfig import BrowserConfig
#导入页面元素相关类
from Tools.Selenium_WebElement import Selenium_WebElement
from Tools.selenium_mouse import selenium_mouse
from Tools.Selenium_WebElement import Selenium_WebElement
#from Tools.PythonHelpApi import PythonHelpApi
#定义类并继承TestCase类
class ShopCardTestCase(unittest.TestCase):
    #修饰以类的方式运行
    @classmethod
    #继承TestCase类中setUpClass方法，该方法只运行一次，且最先运行
    def setUpClass(self):
        #真正实例化代码段
        self.URL = "http://192.168.0.23/tiny/"
        #类的实例化，调用输入URL方法，并传递域名
        BrowserConfig().BrowserGetUrl(self.URL)

    # 修饰以类的方式运行
    @classmethod
    # 继承TestCase类中tearDownClass方法，该方法只运行一次，且最后运行
    def tearDownClass(cls):
        #真正结束清理代码段
        BrowserConfig().BrowserQuit()
    #继承TestCase类中setUp方法，代表初始化，在test方法前运行前必先运行一次
    def setUp(self):
        BrowserConfig().BrowserGetUrl(self.URL)

    # 继承TestCase类中tearDown方法，代表结束清理的含义，在test方法运行后必运行一次
    def tearDown(self):
        pass
    #用例名开头必须以test开头，且用例执行先后顺序遵循unittest框架中main函数的规则
    def testShopCaed002(self):
        #类的实例化，调用具体方法
        a=Selenium_WebElement().Element_Class(PythonHelpApi().ReadExcelData("fristPage",4,2),PythonHelpApi().ReadExcelData("fristPage",4,3))
        Selenium_Mouse().Mouse_move_to_element(a)
        time.sleep(1)
        b=Selenium_WebElement().Element_Xpath('//ul[@class="category"]/li[1]/a')
        Selenium_Mouse().Mouse_move_to_element(b)
        time.sleep(1)
        Selenium_WebElement().Element_LinkTexts("衬衫",0).click()
        time.sleep(1)
        Selenium_WebElement().Element_ClassS("product",0,"商品列表第一件商品未被定位到").click()
        time.sleep(1)
        Selenium_WebElement().Element_Xpath("/html/body/div[3]/div[2]/div[1]/div[3]/div/dl[1]/dd/ul/li[1]/span").click()
        Selenium_WebElement().Element_Xpath("/html/body/div[3]/div[2]/div[1]/div[3]/div/dl[2]/dd/ul/li[1]/span").click()
        Selenium_WebElement().Element_id("add-cart").click()
        expValue="红色"
        c=Selenium_WebElement().Element_id("shopping-cart")
        Selenium_Mouse().Mouse_move_to_element(c)
        time.sleep(1)
        actValue=Selenium_WebElement().Element_Xpath("/html/body/div[2]/div[2]/div[3]/div/div/ul/div/div[2]/p[1]").text
        try:
            self.assertEqual(actValue,expValue)
        except Exception as err:
            assert False,\
                "预期结果为:%s,实际结果为:%s"%(expValue,actValue)

    def testShopCaed001(self):
        expValue = PythonHelpApi().ReadXmlData("ShopCardTestCase","testShopCaed001","expValue")
        c = Selenium_WebElement().Element_id(PythonHelpApi().ReadExcelData("fristPage",1,2))
        Selenium_Mouse().Mouse_move_to_element(c)
        time.sleep(1)
        actValue = Selenium_WebElement().Element_Xpath(PythonHelpApi().ReadXmlData("ShopCardTestCase","testShopCaed001","actValue")).text
        try:
            self.assertEqual(actValue,expValue)
        except Exception as Err:
            assert False,\
                "预期结果为:%s,实际结果为:%s"%(expValue,actValue)
    def testShopCaed003(self):
        print(1)
    def testShopCaed004(self):
        print(2)


#定义主函数
# if __name__ == '__main__':
#     # unittest.main()#main函数执行用例
#     #定义测试套件
#     ShopCardSuite=unittest.TestSuite()
#     #添加用例到测试套件
#     ShopCardSuite.addTest(ShopCardTestCase("testShopCaed004"))
#     ShopCardSuite.addTest(ShopCardTestCase("testShopCaed001"))
#     ShopCardSuite.addTest(ShopCardTestCase("testShopCaed003"))
#     #运行测试套件
#     unittest.TextTestRunner().run(ShopCardSuite)