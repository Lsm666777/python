from selenium import webdriver
import unittest,time
from Units.BrowserAction import BrowserAction
class CompanyDztz(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(1)
        self.driver.get('https://www.baidu.com')
        time.sleep(1)
        self.driver.maximize_window()

        time.sleep(1)
        self.driver.get('test-lsm.51zhongzi.com:7010/pos')

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

    def teComyanyDztz001(self):
        time.sleep(1)
        self.driver.find_element_by_id("username").send_keys(13212345678)

        time.sleep(1)
        self.driver.find_element_by_id("password").send_keys(111111)

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="login"]/button').click()
        time.sleep(1)
        # 商家管理页面
        # driver.find_element_by_xpath('//*[@id="80"]/a').click()
        # 商品管页面
        self.driver.find_element_by_link_text('商品管理').click()

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menus"]/li[3]/a').click()

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="submenus_8303"]/li[1]/a').click()

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="dyntable_length"]/a').click()
        time.sleep(1)
        # 添加商品品牌；品牌名称
        self.driver.find_element_by_id('itemBrand_name').send_keys("测试自动化111")

        time.sleep(1)
        # 品牌备注
        self.driver.find_element_by_name('itemBrand.remark').send_keys("路杉明自动化测试")

        # 点击提交按钮
        self.driver.find_element_by_xpath('//*[@id="logisticForm"]/p[3]/button').click()

        time.sleep(1)
        # 断言
        expValue = "商品品牌添加成功"
        # 通过xpat属性获取页面元素，并获取对应元素的文本值，赋给变量（实际结果）

        time.sleep(1)
        actValue = driver.find_element_by_id('div_message_content').text
        print(actValue)
        # 对比预期结果和实际结果
        if expValue == actValue:
            print("商品品牌添加成功")
        else:
            print("商品品牌添加失败")

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="div_message"]/a').click()

        time.sleep(1)
        # 单位设置
        self.driver.find_element_by_xpath('//*[@id="submenus_8303"]/li[2]/a').click()

        time.sleep(1)
        # 新增商品单位
        self.driver.find_element_by_xpath('//*[@id="dyntable_length"]/a').click()

        time.sleep(1)
        self.driver.find_element_by_id('dict_name').send_keys("箱")

        time.sleep(1)
        self.driver.find_element_by_name('dict.remart').send_keys("50块钱一箱")

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="logisticForm"]/p[3]/button').click()

        time.sleep(1)
        # 断言
        expValue = "商品单位添加成功"

        time.sleep(1)  # 通过xpat属性获取页面元素，并获取对应元素的文本值，赋给变量（实际结果）
        actValue = self.driver.find_element_by_id('div_message_content').text
        print(actValue)
        # 对比预期结果和实际结果
        if expValue == actValue:
            print("单位设置成功")
        else:
            print("单位设置失败")

        time.sleep(1)
        # 叉掉弹窗
        self.driver.find_element_by_xpath('//*[@id="div_message"]/a').click()

        time.sleep(1)
        # 商家管理页面
        self.driver.find_element_by_link_text("商家管理").click()

        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="menus"]/li[1]/a').click()

        time.sleep(1)
        # 填写基本信息，商家名称
        self.driver.find_element_by_id('company_name').send_keys()

        time.sleep(1)
        # 类型
        self.driver.find_element_by_name('company.types').find_element(1)

        time.sleep(1)
        # 是否为集团公司
        self.driver.find_element_by_name('company.isGroup').click()

        time.sleep(1)
        # 简称
        self.driver.find_element_by_id('symbol').send_keys("azw")

        time.sleep(1)
        # 组织机构代码
        self.driver.find_element_by_id('orgaCode').send_keys("54654645")

        time.sleep(1)
        # 营业执照
        self.driver.find_element_by_id('businessLicence').send_keys("465434")

        time.sleep(1)
        # 联系人
        self.driver.find_element_by_id('contact').send_keys("cheng152")

        time.sleep(1)
        # 点子邮箱
        self.driver.find_element_by_id('contact').send_keys("546546@qq.com")

        time.sleep(1)
        # 手机号码
        self.driver.find_element_by_id('mob').send_keys("13315274421")

        time.sleep(1)
        # 电话
        self.driver.find_element_by_id('tel').send_keys("5644331")

        time.sleep(1)
        # 客服电话
        self.driver.find_element_by_id('serviceTel').send_keys("5644331")

        time.sleep(1)
        # 办公地址
        self.driver.find_element_by_xpath('//*[@id="r_province"]/option[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="r_city"]/option[2]').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="company_region"]/option[4]').click()
        time.sleep(1)
        self.driver.find_element_by_name('company.address').send_keys("望京SOHO")

        time.sleep(1)
        # 招商人员
        self.driver.find_element_by_xpath('//*[@id="selection2"]/option[3]').click()

        time.sleep(1)
        # 商家简介
        self.driver.find_element_by_id('companyDesc').send_keys("非家村家园共育")

        time.sleep(1)
        # 下一步
        self.driver.find_element_by_xpath('//*[@id="wizard"]/div[2]/a[2]').click()


if __name__=='__main__':
    unittest.main()













