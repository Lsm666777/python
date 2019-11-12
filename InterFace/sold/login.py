
import unittest
import os
import HTMLTestRunner
import json
import requests
from InterFace.Study.Request import RunMain
from InterFace.tool.GetRessponse import GetRessponse
from InterFace.tool.GetRessponse import AnalysisResponse
from InterFace.Study.runmethod import RunMethod
class TestMethod(unittest.TestCase):
    # 修饰以类的方式运行
    @classmethod
    # 继承TestCase类中setUpClass方法，该方法只运行一次，且最先运行
    def setUpClass(self):
        pass

    # 修饰以类的方式运行
    @classmethod
    # 继承TestCase类中tearDownClass方法，该方法只运行一次，且最后运行
    def tearDownClass(cls):
        pass
    #继承TestCase类中setUp方法，代表初始化，在test方法前运行前必先运行一次
    def setUp(self):
        url = 'http://192.168.1.137:8080/sold/app/login'
        # 请求参数
        data = {
            'code': '111111',
            'mob': '17800000000',
            'positionX': '116.480153',
            'positionY': '39.997075',
        }

        self._respons = RunMethod().run_main('post',url,data)
        print(json.dumps(self._respons,ensure_ascii=False,sort_keys=True,indent=2))
        globals()['response'] = self._respons
        self._storeid = globals()['response']["data"]["storeId"]

        self._JSESSIONID = globals()['response']["data"]["jsessionid"]
        self._access_token = globals()['response']["data"]["access_token"]
        print(self._storeid,self._JSESSIONID,self._access_token)
    # 继承TestCase类中tearDown方法，代表结束清理的含义，在test方法运行后必运行一次
    def tearDown(self):
        pass

    # 用例名开头必须以test开头，且用例执行先后顺序遵循unittest框架中main函数的规则
    @unittest.skip('test_001')
    #获取区域
    def test_001(self):
        _url = 'http://192.168.1.137:8080/sold/app/store/region'
        # 请求参数
        _data = {
            'parentId': '110101'
        }

        self._respons = RunMethod().run_main('post', _url, _data)

        # print(json.dumps(_respons,ensure_ascii=False,sort_keys=True,indent=2))

        # 验证http状态码200
        # self.assertEqual(200,_suatuscose,'suatuscose is error')
        # 验证resuit返回状态码200
        self.assertEqual(200,self._respons['result']['code'], msg="_response['result']['code'] is error")
        # 验证result返回信息
        self.assertEqual('获取区域成功！',self._respons['result']['message'], msg="_response['result']['code'] is error")

    #门店设置
    def test_store_setting004(self):
        url = "http://192.168.1.137:8080/sold/app/getcode"
        data = {
            'storeId': '42'
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        response = RunMethod().run_main('post', url, data,header)
        self.assertEqual(200, response['result']['code'], msg="response['result']['code'] is error")
        self.assertEqual('获取门店详情成功！', response['result']['message'], msg="response['result']['message'] is error")


    #获取商品分类列表
    # @unittest.skip('test_002')   #调过不执行这条用例
    def test_002(self):

        url = 'http://192.168.1.137:8080/sold/app/orders/categorylist'
        data = {
            'storeId':self._storeid
        }
        header = {
            "Authorization":self._access_token,
            "jsessionid":self._JSESSIONID
        }

        _respons = RunMethod().run_main('post',url,data,header)
        print(json.dumps(_respons, ensure_ascii=False, sort_keys=True, indent=2))

        # 验证resuit返回状态码200
        self.assertEqual(200,_respons['result']['code'],msg="_response['result']['code'] is error")
        # 验证result返回信息
        self.assertEqual('登录成功！',self._respons['result']['message'],msg="_response['result']['code'] is error")


    #登录获取验证码
    def test_get_code003(self):
        url = "http://192.168.1.137:8080/sold/app/getcode"
        data = {
            'mob':'13212345678'
        }
        response = RunMethod().run_main('post',url,data)
        self.assertEqual(200,response['result']['code'],msg="response['result']['code'] is error")
        self.assertEqual('获取验证码成功！',response['result']['message'], msg="response['result']['message'] is error")


        # 退出登录
        # @unittest.skip('test_003')
    def test_005(self):
        url = 'http://192.168.1.137:8080/sold/app/logout'
        data = {
            'storeId': self._storeid
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data, header)
        # 将返回参数转换为json格式

        # 验证http状态码200
        # self.assertEqual(200, AnalysisResponse(_respons).getstatuscode, 'suatuscose is error')
        # 验证result返回状态码200

        self.assertEqual('200', str(_respons['result']['code']), msg="_response['result']['code' is error")
        # 验证result返回信息
        self.assertEqual('退出登录成功！', str(_respons['result']['message']), msg="_response['result']['message'] is error")

    #客户列表
    def test_get_client006(self):
        url = 'http://192.168.1.137:8080/sold/app/customer/customerlist'
        data = {
            'storeId': self._storeid
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data, header)
        # 将返回参数转换为json格式

        # 验证http状态码200
        # self.assertEqual(200, AnalysisResponse(_respons).getstatuscode, 'suatuscose is error')
        # 验证result返回状态码200

        self.assertEqual('200', str(_respons['result']['code']), msg="_response['result']['code' is error")
        # 验证result返回信息
        self.assertEqual('获取成功！', str(_respons['result']['message']), msg="_response['result']['message'] is error")

    #添加客户
    def test_add_client007(self):

        url = 'http://192.168.1.137:8080/sold/app/customer/add'
        data = {
            'storeId': self._storeid,
            'phone': '17800000000',
            'name': '王先生',
            'address': '北京市朝阳区',
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data, header)

        # 验证http状态码200
        # self.assertEqual(200, AnalysisResponse(_respons).getstatuscode, 'suatuscose is error')
        # 验证result返回状态码200

        self.assertEqual('200', str(_respons['result']['code']), msg="_response['result']['code' is error")
        # 验证result返回信息
        self.assertEqual('获取成功！', str(_respons['result']['message']), msg="_response['result']['message'] is error")

    #删除客户
    def test_delete_client008(self):
        url = 'http://192.168.1.137:8080/sold/app/customer/del'
        data = {
            'storeId': self._storeid,
            'id': '17800000000',

        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data, header)
        # 将返回参数转换为json格式

        # 验证http状态码200
        # self.assertEqual(200, AnalysisResponse(_respons).getstatuscode, 'suatuscose is error')
        # 验证result返回状态码200

        self.assertEqual('200', str(_respons['result']['code']), msg="_response['result']['code' is error")
        # 验证result返回信息
        self.assertEqual('获取成功！', str(_respons['result']['message']), msg="_response['result']['message'] is error")


if __name__ == '__main__':
    unittest.main()

    # suite = unittest.TestSuite()
    # suite.addTest(TestMethod('test_001'))
    # suite.addTest(TestMethod('test_002'))
    # suite.addTest(TestMethod('test_003'))
    # # unittest.TextTestRunner().run(suite)
    #
    # #文件报告路径
    # filepath = "D:/python/Lsm/InterFace/htmltestrunner1.html"
    # fp = open(filepath,'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="这是一份接口测试报告！",description="这是第一次测试报告！",verbosity=2)
    # runner.run(suite)