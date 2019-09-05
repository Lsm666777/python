import unittest,time,os
from item.Appcode.PackagingElement.LogonPageIndex import LogonPageIndex
from Utils.GetAppiumIndex import getAppiumIndex
from item.Appcode.PackagingElement.datables import datables
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
        #os.system("com.android.inputmethod.latin/.LatinIME")
        LogonPageIndex().PhoneNumber()
        time.sleep(1)
        LogonPageIndex().verifycode()
        time.sleep(1)
        LogonPageIndex().login()
        __expValue = datables()
        # __expValue = "种子销售电子台账系统"
        __actvalue = self.driver.find_element_by_id('com.azhyun.saas.e_account:id/user_name_text_view').text
        try:
            self.assertEqual(__actvalue,__expValue)
        except Exception as err:
            assert False,\
                "预期结果为:%s,实际结果为:%s" % (__expValue,__actvalue)

if __name__ == '__main__':
    unittest.main()

