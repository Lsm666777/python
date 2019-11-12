from Utils.GetAppiumIndex import getAppiumIndex
from item.FarmersTakeOn.AppPackage.Login import loginpage
import unittest,time
class testloginIndex(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = getAppiumIndex().driver
    @classmethod
    def tearDownClass(self):
        self.driver.quit()
    def setUp(self):
        pass
        #self.driver = getAppiumIndex().driver
    def tearDown(self):
        pass
        #time.sleep(3)
        #self.driver.quit()
    def testlogin001(self):
        time.sleep(5)
        loginpage().account()




# if __name__ == '__main__':
#         unittest.main()
