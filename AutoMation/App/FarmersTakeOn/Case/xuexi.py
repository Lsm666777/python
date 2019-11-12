from appium import webdriver
# from selenium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.0'
desired_caps['deviceName'] = 'FRD_AL00'
desired_caps['appPackage'] = 'com.example.nft.nftongapp'
desired_caps['appActivity'] = '.activity.LoginActivity'
# desired_caps['unicodeKeyboard'] = 'True'
# desired_caps['resetKeyboard'] = 'True'
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#打开通知栏
# driver.open_notifications()
#打开安卓设备上的位置定位设置
# driver.toggle_location_services()
#设置设备的经纬度
# driver.set_location()
#获取当前页面的网址
# print(driver.current_url)

#点击
driver.tap([(520,1600)])