from appium import webdriver
from Tools.Selenium_WebElement import Selenium_WebElement

Selenium_WebElement.
import time
import os
import sys

from Tools.Common import singleton
# @singleton
# class initialize(object):
#     def __init__(self):
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '7.0'
# desired_caps['deviceName'] = 'FRD_AL00'
# desired_caps['appPackage'] = 'com.example.loveamall'
# desired_caps['appActivity'] = '.activity.SplashActivity'
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
# #
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'FRD_AL00'
desired_caps['appPackage'] = 'com.azhyun.saas.e_account'
desired_caps['appActivity'] = '.activity.SplashActivity'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

time.sleep(3)


#注册
# driver.find_element_by_id("com.azhyun.saas.e_account:id/btn_register").click()
# os.system("com.android.inputmethod.latin/.LatinIME")
# driver.find_element_by_id("com.azhyun.saas.e_account:id/deit_store_name").send_keys("爱种网络")



driver.find_element_by_id("com.azhyun.saas.e_account:id/et_phone").send_keys("17800000000")

driver.find_element_by_id("com.azhyun.saas.e_account:id/et_code").send_keys(111111)

#time.sleep(1)
driver.find_element_by_id("com.azhyun.saas.e_account:id/btn_login").click()

#点击添加台账
time.sleep(1)
# driver.find_element_by_link_text("添加台账").click()
driver.tap([(230,610)])


# driver.tap([(800,600)])
# time.sleep(1)
# #添加客户
# driver.find_element_by_id("com.azhyun.saas.e_account:id/title_add").click()
#
# time.sleep(1)
# driver.find_element_by_id("com.azhyun.saas.e_account:id/edt_name").send_keys("路杉明")
#
# driver.find_element_by_id("com.azhyun.saas.e_account:id/edt_card").send_keys("130627199802061212")
#
# driver.find_element_by_id("com.azhyun.saas.e_account:id/edt_address").send_keys("望京")
#
# driver.find_element_by_id("com.azhyun.saas.e_account:id/edt_phone").send_keys("13582286364")
#
# driver.find_element_by_id("com.azhyun.saas.e_account:id/btn").click()


#添加台账
#输入姓名
#time.sleep(1)
driver.find_element_by_id("com.azhyun.saas.e_account:id/edt_name").send_keys('路杉明')
#time.sleep(1)
driver.find_element_by_id("com.azhyun.saas.e_account:id/edt_card").send_keys("130627199802061212")
#time.sleep(1)
driver.find_element_by_id("com.azhyun.saas.e_account:id/edt_address").send_keys("北京市朝阳区")
#time.sleep(1)
driver.find_element_by_id("com.azhyun.saas.e_account:id/edt_phone").send_keys("15832217533")
#time.sleep(1)
driver.find_element_by_id("com.azhyun.saas.e_account:id/btn_next").click()

#添加商品信息
driver.find_element_by_id('com.azhyun.saas.e_account:id/image_add_goods').click()
#选择第一个商品
driver.find_elements_by_id('com.azhyun.saas.e_account:id/select')[0].click()

driver.find_elements_by_id('com.azhyun.saas.e_account:id/select')[1].click()
#点击确认选择
driver.find_element_by_id('com.azhyun.saas.e_account:id/btn_confirm').click()

#点击保存
driver.find_element_by_id('com.azhyun.saas.e_account:id/btn_save').click()


# driver.swipe(800, 1300, 100, 1300, 1000)
# time.sleep(2)
# driver.swipe(800, 1300, 100, 1300, 1000)
# time.sleep(3)
#
# driver.tap([(550,1520)])
# time.sleep(1)
# driver.tap([(819,1700)])




# time.sleep(5)
#
#
#
# driver.quit()