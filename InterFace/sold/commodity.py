import unittest
import json
from InterFace.Study.runmethod import RunMethod
class Commodity(unittest.TestCase):
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
        # print(self._storeid, self._JSESSIONID, self._access_token)

    def tearDown(self):
        pass

    #添加分类
    def test_case01(self):
        url = 'http://192.168.1.137:8080/sold/app/item/addcategory'
        # 请求参数
        data = {
            'storeId': self._storeid,
            'name': '山1'
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data,header)


        # 验证resuit返回状态码200
        self.assertEqual('200', _respons['result']['code'], msg="_response['result']['code'] is error")
        # 验证result返回信息
        self.assertEqual('添加分类成功！', _respons['result']['message'], msg="_response['result']['code'] is error")
    #获取分类列表
    def test_case02(self):
        url = 'http://192.168.1.137:8080/sold/app/item/categorylist'
        # 请求参数
        data = {
            'storeId': self._storeid
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data, header)
        print(_respons['data'][0]['id'])
        # print(_respons)
        # 验证resuit返回状态码200
        self.assertEqual('200', _respons['result']['code'], msg="_response['result']['code'] is error")
        # 验证result返回信息
        self.assertEqual('获取商品分类列表成功！', _respons['result']['message'], msg="_response['result']['code'] is error")

    #商品的列表
    def test_case03(self):
        url = 'http://192.168.1.137:8080/sold/app/item/list'
        # 请求参数
        data = {
            'storeId': self._storeid,
            'categoryId':'0',
            'pageNo':'1',
            'pageSize':'10'
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data, header)

        # 验证resuit返回状态码200
        self.assertEqual('200', _respons['result']['code'], msg="_response['result']['code'] is error")
        # 验证result返回信息
        self.assertEqual('查询成功！', _respons['result']['message'], msg="_response['result']['code'] is error")

    #品种的列表
    def test_case004(self):
        url = 'http://192.168.1.137:8080/sold/app/item/variety'
        # 请求参数
        data = {
            'id': '1',
            'pageNo': '1',
            'pageSize': '10'
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data, header)

        # 验证resuit返回状态码200
        self.assertEqual('200', _respons['result']['code'], msg="_response['result']['code'] is error")
        # 验证result返回信息
        self.assertEqual('获取品种列表成功！', _respons['result']['message'], msg="_response['result']['code'] is error")

    #商品的添加
    def test_case005(self):
        url = 'http://192.168.1.137:8080/sold/app/item/save'
        # 请求参数
        data = {
            'id': '1',
            'pageNo': '1',
            'pageSize': '10'
        }
        header = {
            "Authorization": self._access_token,
            "jsessionid": self._JSESSIONID
        }
        _respons = RunMethod().run_main('post', url, data, header)

        # 验证resuit返回状态码200
        self.assertEqual('200', _respons['result']['code'], msg="_response['result']['code'] is error")
        # 验证result返回信息
        self.assertEqual('获取品种列表成功！', _respons['result']['message'], msg="_response['result']['code'] is error")


if __name__ == '__main__':
    unittest.main()