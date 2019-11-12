
import unittest

import json
from InterFace.Study.runmethod import RunMethod
array = []
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
        self._respons = RunMethod().run_main('post', url, data)
        # print(json.dumps(self._respons, ensure_ascii=False, sort_keys=True, indent=2))
        globals()['response'] = self._respons
        self._storeid = globals()['response']["data"]["storeId"]
        self._JSESSIONID = globals()['response']["data"]["jsessionid"]
        self._access_token = globals()['response']["data"]["access_token"]
    # 继承TestCase类中tearDown方法，代表结束清理的含义，在test方法运行后必运行一次
    def tearDown(self):
        pass

    # 客户列表
    def test_get_client001(self):
        url = 'http://192.168.1.137:8080/sold/app/customer/customerlist'
        data = {
            'storeId': self._storeid
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data, header)
        # print(json.dumps(_respons,ensure_ascii=False,sort_keys=True,indent=2))
        # globals()['key'] = _respons #['data'][0]['list'][0]['id']
        array.append(_respons['data'][0]['list'][0]['id'])

        print(array)
        # 验证http状态码200
        # self.assertEqual(200, AnalysisResponse(_respons).getstatuscode, 'suatuscose is error')
        # 验证result返回状态码200

        self.assertEqual('200', str(_respons['result']['code']), msg="_response['result']['code'] is error")
        # 验证result返回信息
        self.assertEqual('获取成功！', str(_respons['result']['message']), msg="_response['result']['message'] is error")

    # 添加客户
    @unittest.skip('test_add_client002')
    def test_add_client002(self):
        print(a)

        url = 'http://192.168.1.137:8080/sold/app/customer/add'
        data = {
            'storeId': self._storeid,
            'phone': 13277884565,
            'name': '王12先',
            'address': '北京市朝阳区',
            'ID_number':''
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data, header)


        # 验证http状态码200
        # self.assertEqual(200, AnalysisResponse(_respons).getstatuscode, 'suatuscose is error')
        # 验证result返回状态码200

        self.assertEqual('200',str(_respons['result']['code']), msg="_response['result']['code' is error")
        # 验证result返回信息
        self.assertEqual('添加客户成功！',str(_respons['result']['message']), msg="_response['result']['message'] is error")

    # 删除客户
    # @unittest.skip('test_delete_client003')
    def test_delete_client003(self):
        # store_id = globals()['key']

        url = 'http://192.168.1.137:8080/sold/app/customer/del'
        data = {
            'storeId': self._storeid,
            'id': array,

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

        self.assertEqual('200',str(_respons['result']['code']), msg="_response['result']['code' is error")
        # 验证result返回信息
        self.assertEqual('获取成功！',str(_respons['result']['message']), msg="_response['result']['message'] is error")
if __name__ == '__main__':
    unittest.main()