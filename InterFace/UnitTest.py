import unittest
from InterFace.tool.GetRessponse import GetRessponse
from InterFace.tool.GetRessponse import AnalysisResponse
from InterFace.tool.AnalysisBusingess import AnalysisBusingess
from InterFace.Study.Request import RunMain
class TestMethod(unittest.TestCase):
    # 修饰以类的方式运行
    @classmethod
    # 继承TestCase类中setUpClass方法，该方法只运行一次，且最先运行
    def setUpClass(self):

        self._url = 'http://192.168.1.137:8080/sold/app/login'
        # 请求参数
        self._data = {
            'code': '111111',
            'mob': '17800000000',
            'positionX': '116.480153',
            'positionY': '39.997075',
        }
        self.business = AnalysisBusingess()
    # 修饰以类的方式运行
    @classmethod
    # 继承TestCase类中tearDownClass方法，该方法只运行一次，且最后运行
    def tearDownClass(cls):
        pass
    #继承TestCase类中setUp方法，代表初始化，在test方法前运行前必先运行一次
    def setUp(self):
        pass
        # _url = 'http://192.168.1.137:8080/sold/app/login'
        # #请求参数
        # _data = {
        #     'code':'111111',
        #     'mob':'17800000000',
        #     'positionX':'116.480059',
        #     'positionY':'39.997195',
        # }
        # self.response = GetRessponse(_url,_data).getResponse()

    # 继承TestCase类中tearDown方法，代表结束清理的含义，在test方法运行后必运行一次
    def tearDown(self):
        pass

    # 用例名开头必须以test开头，且用例执行先后顺序遵循unittest框架中main函数的规则
    def test001(self):

        _exp = 200
        self.business.assertStatusCode(_url=self._url, _param=self._data, _exp=_exp)
    # def test002(self):
        _exp = 200
        self.business.assertResultcode(_url=self._url, _param=self._data, _exp=_exp,_method='post')

        # rvRespomse = AnalysisResponse(self.response)

        # 验证状态码200
        # self.assertEqual(200,rvRespomse.getstatuscode,msg="status_code is error")
        #转换为json格式
        # Ressponse = rvRespomse.dicResponse
        # a = Ressponse['result']['code']
        # print(a)
        #验证返回信息"登录成功!"
        # self.assertEqual('登录成功！',str(Ressponse['result']['message']),msg="Ressponse['result']['message'] is error")
        #验证店铺名称
        # self.assertEqual('艾欧尼亚',str(Ressponse['data']['name']),msg="Ressponse['data']['name'] is error")
        # # 验证店铺ID
        # self.assertEqual(42, int(Ressponse['data']['storeId']), msg="Ressponse['data']['storeId'] is error")
        # #验证店铺状态
        # self.assertEqual(1, int(Ressponse['data']['status']), msg="Ressponse['data']['status'] is error")

if __name__ == '__main__':
    unittest.main()