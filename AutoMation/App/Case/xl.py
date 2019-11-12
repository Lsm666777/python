
#导入webdriver类库（来自于那个包导入那个类）
from selenium import webdriver
# 导入时间类库
import time
#使用webdriver协议，链接火狐浏览器
#driver=webdriver.Firefox()
driver=webdriver.Chrome()
#获取域名在浏览器中打开（get是webdriver中函数，获取浏览器域名）
driver.get('https://www.baidu.com')
#休息1秒
time.sleep(1)
#浏览器窗口最大化（maximize_window是webdriver中函数，窗口最大化函数）
driver.maximize_window()

#通过name属性查找页面元素，并输入
driver.get('test-lsm.51zhongzi,com:7010/pos')
#driver.find_element_by_name("wd").send_keys("test-lsm.51zhongzi.com:7010/pos")
# driver.find_element_by_id("wd").send_keys("建国大业")
#通过ID属性查找页面元素，并点击
driver.find_element_by_id("su").click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="article"]/div/a[1]').click()
time.sleep(1)
driver.find_element_by_name("az_username").text("15832217533")




#预期结果




#expValue="爱种网"
#通过xpat属性获取页面元素，并获取对应元素的文本值，赋给变量（实际结果）
#actValue=driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/div/h3/a/em").text
#print(actValue)
#对比预期结果和实际结果
#if expValue == actValue:
#    print("pass")
#else:
#    print("Fail")

#退出浏览器
#driver.quit()





#导入webdriver类库（来自于那个包导入那个类）
#from selenium import webdriver
# 导入时间类库
#import time
#使用webdriver协议，链接火狐浏览器
#driver=webdriver.Chrome()
#获取域名在浏览器中打开（get是webdriver中函数，获取浏览器域名）
#driver.get('https://www.baidu.com')
#休息1秒
#time.sleep(1)
#浏览器窗口最大化（maximize_window是webdriver中函数，窗口最大化函数）
#driver.maximize_window()
#通过name属性查找页面元素，并输入
#driver.find_element_by_name("wd").send_keys("建国大业")

# driver.find_element_by_id("wd").send_keys("建国大业")
#通过ID属性查找页面元素，并点击
#driver.find_element_by_id("su").click()
#time.sleep(1)
#获取当前页面序列号
#handle=driver.current_window_handle
#点击播放按钮
#driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/div[1]/a/i").click()
#等待15秒
#time.sleep(15)
#获取所有页面序列号
#allhandle=driver.window_handles
#当前序列号在所有序列号中
#for tmp in allhandle:
    # 对比当前序列号不等于之前序列号
 #   if tmp != handle:
        #切换到当前页面
  #      driver.switch_to_window(tmp)
#expValue="建国大业"
#actValu=driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div/div[1]/div[1]/div[1]/div/h2").text
#print(actValu)
#if expValue in actValu:
#    print("pass")
#else:
#    print("Fail")
#driver.quit()


# #预期结果
# expValue="建国大业"
# #通过xpat属性获取页面元素，并获取对应元素的文本值，赋给变量（实际结果）
# actValue=driver.find_element_by_xpath("/html/body/div[1]/div[5]/div[1]/div[3]/div[1]/div/h3/a/em").text
# print(actValue)
# #对比预期结果和实际结果
# if expValue == actValue:
#     print("pass")
# else:
#     print("Fail")
#退出浏览器
#driver.quit()


#新的API练习

# driver.contexts
driver.current_url    

