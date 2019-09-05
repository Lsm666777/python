from selenium import webdriver
import time
from Tools.Selenium_WebElement import Selenium_WebElement

dr = webdriver.Chrome()
dr.maximize_window()
dr.get("http://it-lsm.51zhongzi.com:9000/land/login")
time.sleep(1)
dr.find_element_by_id("username").send_keys(13212345678)
dr.find_element_by_id("password").send_keys(111111)
dr.find_element_by_xpath('//*[@id="login_form"]/div[3]/input').click()
time.sleep(2)
name = dr.find_element_by_class_name("active").text
values = "欢迎"
if name == values:
    print("用户登录成功")
else:
    print("用户登录失败")

dr.find_element_by_link_text("供需信息管理").click()

dr.find_element_by_link_text("供需分类管理").click()

dr.find_element_by_xpath('//*[@id="dynamic-table_wrapper"]/div[1]/div/button').click()
time.sleep(2)
#切换iframe
iframe = dr.find_element_by_tag_name("iframe")
dr.switch_to_frame(iframe)
dr.find_element_by_name("name").send_keys("自动化测试")

dr.find_element_by_xpath('//*[@id="ex"]/div[2]/div/button[1]').click()
time.sleep(1)

name1 = dr.find_element_by_xpath('//*[@id="gp-table"]/tbody/tr[1]/td[2]').text
values1 = "自动化测试"
if name1 == values1:
    print("供需分类添加成功")
else:
    print("供需分类添加失败")
time.sleep(1)
#点击修改按钮
dr.find_element_by_xpath('//*[@id="gp-table"]/tbody/tr[1]/td[4]/a[1]').click()
time.sleep(1)

#转换iframe
frame = dr.find_element_by_tag_name("iframe")

dr.switch_to_frame(frame)

dr.find_element_by_id("name").send_keys("测试")

time.sleep(2)

dr.close()
