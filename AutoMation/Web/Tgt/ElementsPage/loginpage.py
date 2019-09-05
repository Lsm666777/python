#导入浏览器相关类（导入后具体业务场景使用该类下的属性或方法）
from Tools.BrowserConfig import BrowserConfig
#导入页面元素相关类
from Tools.Selenium_WebElement import Selenium_WebElement
from Tools.selenium_mouse import selenium_mouse
from Tools.Selenium_WebElement import Selenium_WebElement
#from Tools.PythonHelpApi import PythonHelpApi

class loginpage(object):
#登录用例
    def login(self):
        Selenium_WebElement().Element_id("username").send_keys(13212345678)
        Selenium_WebElement().Element_name("j_password").send_keys(111111)
        Selenium_WebElement().Element_Xpath('//*[@id="login_form"]/div[3]/input').click()
        expValue = "欢迎"
        actValue = Selenium_WebElement().Element_class("active").text
        try:
            self.assertEqual(actValue,expValue)
        except Exception as err:
            assert False, \
                "预期结果为:%s,实际结果为:%s" % (expValue,actValue)

#密码不正确时登录用例
    def errorpassword(self):
        # Selenium_WebElement().Element_id("username").send_keys(13212345678)
        # Selenium_WebElement().Element_name("j_password").send_keys(11111111)
        # Selenium_WebElement().Element_Xpath('//*[@id="login_form"]/div[3]/input').click()
        # expValue = "登录失败，错误的手机号码或密码！"
        # actValue = Selenium_WebElement().Element_class("loginmsg").text
        # try:
        #     self.assertEqual(actValue, expValue)
        # except Exception as err:
        #     assert False, \
        #         "预期结果为:%s,实际结果为:%s" % (expValue, actValue)
        Selenium_WebElement().Element_Text("系统管理").click()
        Selenium_WebElement().Element_Text("个人信息").click()
        Selenium_WebElement().Element_Text("查看个人信息").click()
        actValues = Selenium_WebElement().Element_Xpath('//*[@id="body_content"]/form/div[1]/label[2]').text
        expValues = "SA "
        try:
            self.assertEqual(actValues,expValues)
        except Exception as err:
            assert False,\
                "预期结果为:%s,实际结果为:%s"%(expValues,actValues)




