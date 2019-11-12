from selenium import webdriver
import time
driver = webdriver.Chrome()

time.sleep(1)
driver.get('https://www.baidu.com')
time.sleep(1)
driver.maximize_window()

time.sleep(1)
driver.get('test-lsm.51zhongzi.com:7090/cold')

time.sleep(1)
driver.find_element_by_id("username").send_keys(13212345678)

time.sleep(1)
driver.find_element_by_id("password").send_keys(111111)
#登陆
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/input').click()
#门店管理
time.sleep(1)
driver.find_element_by_xpath('//*[@id="func11"]/a').click()

driver.find_element_by_xpath('//*[@id="func1101"]/a').click()

