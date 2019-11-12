from selenium import webdriver
import time
driver = webdriver.Chrome()

time.sleep(1)
driver.get('https://www.baidu.com')
time.sleep(1)
driver.maximize_window()

time.sleep(1)
driver.get('https://saas.51zhong.com')

time.sleep(1)
driver.find_element_by_xpath('//*[@id="login_div"]/a[2]').click()

time.sleep(1)
driver.find_element_by_id('company_name').send_keys("小个s小伙")

time.sleep(1)
driver.find_element_by_xpath('//*[@id="company_types"]/option[2]').click()
time.sleep(1)
#企业简称
driver.find_element_by_id('company_symbol').send_keys("小伙子")
time.sleep(1)
driver.find_element_by_id('company_enAbbreviation').send_keys("xhrxz")
time.sleep(1)
driver.find_element_by_id('company_contact').send_keys("路杉1明")
time.sleep(1)
driver.find_element_by_id('company_mob').send_keys(13399999799)
time.sleep(1)
driver.find_element_by_id('company_password').send_keys(111111)
time.sleep(1)
driver.find_element_by_id('confirm_password').send_keys(111111)
time.sleep(1)
driver.find_element_by_id('company_address').send_keys("望京")

time.sleep(1)
#主营业务
driver.find_element_by_name('categoryName2').click()

driver.find_element_by_name('categoryName3').click()

driver.find_element_by_name('categoryName4').click()

driver.find_element_by_name('categoryName5').click()

driver.find_element_by_name('categoryName6').click()

driver.find_element_by_name('categoryName7').click()

driver.find_element_by_name('categoryName8').click()
driver.find_element_by_name('categoryName1').click()

driver.find_element_by_name('categoryName9').click()

#登陆
time.sleep(1)
driver.find_element_by_id('register_submit').click()

time.sleep(1)
driver.find_element_by_link_text('企业信息').click()

expValue="种子   肥料   农药   保险   园艺   农机   粮食收购   测土&配肥   农技服务  "

time.sleep(1)#通过xpat属性获取页面元素，并获取对应元素的文本值，赋给变量（实际结果）
actValue=driver.find_element_by_id('div_message_content').text
print(actValue)
#对比预期结果和实际结果
if expValue == actValue:
    print("单位设置成功")
else:
    print("单位设置失败")

#time.sleep(1)
#driver.find_element_by_xpath('//*[@id="body_content"]/div[2]/div/a/img').click()

#time.sleep(1)
#driver.find_element_by_xpath('//*[@id="body_content"]/form/div[1]/div[2]/ul/li[5]/button').click()

#time.sleep(1)
#driver.find_element_by_xpath('//*[@id="body_content"]/div[3]/div[1]/div[2]/ul/li[7]/button[1]').click()

#进入企业空间
#time.sleep(1)
#driver.find_element_by_xpath('//*[@id="body_content"]/div[2]/div[1]/a/img').click()

#time.sleep(3)
#driver.quit()




#time.sleep(1)
#driver.find_element_by_link_text("企业信息").click()
#time.sleep(1)
#driver.find_element_by_xpath('//*[@id="func1001"]/a').click()



