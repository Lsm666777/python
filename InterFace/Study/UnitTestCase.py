#encoding='UTF-8'
import unittest
import os
import HTMLTestRunner
import json
from InterFace.Study.Request import RunMain
from InterFace.tool.GetRessponse import GetRessponse
from InterFace.tool.GetRessponse import AnalysisResponse

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
        pass
    # 继承TestCase类中tearDown方法，代表结束清理的含义，在test方法运行后必运行一次
    def tearDown(self):
        pass

    # 用例名开头必须以test开头，且用例执行先后顺序遵循unittest框架中main函数的规则
    def test_001(self):
        _url = 'http://192.168.1.137:8080/sold/app/login'
        # 请求参数
        _data = {
            'code': '111111',
            'mob': '17800000000',
            'positionX': '116.480153',
            'positionY': '39.997075',
        }

        _respons = GetRessponse(_url,_data,'post').getResponse()
        _response = _respons.json()

        _suatuscose = AnalysisResponse(_respons).getstatuscode
        #验证http状态码200
        self.assertEqual(200,_suatuscose,'suatuscose is error')
        #验证resuit返回状态码200
        self.assertEqual('200',_response['result']['code'],msg="_response['result']['code'] is error")
        #验证result返回信息
        self.assertEqual('登录成功！', _response['result']['message'], msg="_response['result']['code'] is error")
        # print(res)
        #设置全局变量，把参数传给下条Case
        globals()['response'] = _response

                    # response = RunMain().run_main(_url,_data,'post')
                    # print(response)
                    # self.assertEqual(int(res['result']['code']),200,msg="res['result']['code'] is error")
    #获取商品分类列表
    # @unittest.skip('test_002')   #调过不执行这条用例
    def test_002(self):
        _storeid = globals()['response']['data']['storeId']
        _JSESSIONID = globals()['response']['data']['jsessionid']
        _access_token = globals()['response']['data']['access_token']
        _url = 'http://192.168.1.137:8080/sold/app/orders/categorylist'
        _data = {
            'storeId':_storeid,
            'JSESSIONID':_JSESSIONID,
            'Authorization':_access_token
        }
        _respons = GetRessponse(_url,_data,'post').getResponse()
        _response = _respons.json()
        _suatuscose = AnalysisResponse(_respons).getstatuscode
        # 验证http状态码200
        self.assertEqual(200, _suatuscose, '_suatuscose is error')
        # 验证resuit返回状态码200
        self.assertEqual('200', _response['result']['code'], msg="_response['result']['code'] is error")
        # 验证result返回信息
        self.assertEqual('token为空!', _response['result']['message'], msg="_response['result']['code'] is error")
    def test_003(self):
        _storeid = globals()['response']['data']['storeId']
        _data = {
            'storeId':_storeid
        }
        _url = 'http://192.168.1.137:8080/sold/app/logout'
        _respons = GetRessponse(_url,_data,'post').getResponse()
        #将返回参数转换为json格式
        _response = _respons.json()

        # 验证http状态码200
        self.assertEqual(200, AnalysisResponse(_respons).getstatuscode, 'suatuscose is error')
        #验证result返回状态码200
        self.assertEqual('-100',str(_response['result']['code']),msg="_response['result']['code' is error")
        #验证result返回信息
        self.assertEqual('未知错误！',str(_response['result']['message']),msg="_response['result']['message'] is error")
if __name__ == '__main__':
    # unittest.main()

    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_001'))
    suite.addTest(TestMethod('test_002'))
    suite.addTest(TestMethod('test_003'))
    # unittest.TextTestRunner().run(suite)

    #文件报告路径
    filepath = "D:/python/Lsm/InterFace/htmltestrunner111.html"
    fp = open(filepath,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="这是一份接口测试报告！",description="这是第一次测试报告！",verbosity=2)
    runner.run(suite)