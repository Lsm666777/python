from appium import webdriver
from Tools.Common import singleton

@singleton
class getAppiumIndex(object):
    def __init__(self):
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '7.0'
        # desired_caps['deviceName'] = 'FRD_AL00'
        # desired_caps['appPackage'] = 'com.azhyun.saas.e_account'
        # desired_caps['appActivity'] = '.activity.SplashActivity'
        # desired_caps['unicodeKeyboard'] = 'True'
        # desired_caps['resetKeyboard'] = 'True'
        # self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.0'
        desired_caps['deviceName'] = 'FRD_AL00'
        desired_caps['appPackage'] = 'com.example.nft.nftongapp'
        desired_caps['appActivity'] = '.activity.LoginActivity'
        # desired_caps['unicodeKeyboard'] = 'True'
        # desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)