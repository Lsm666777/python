import requests
import json
#获取请求
class GetRessponse(object):
    #接参
    def __init__(self,_url,_param=None,_method='post'):
        self.url = _url
        self.param = _param
        self.method = _method
    #根据method 发送请求
    def getResponse(self):
        if self.method.lower() == 'get':
            _response = requests.get(self.url,params=self.param)
            return _response
        elif self.method.lower() == 'post':
            _response = requests.post(self.url,data=self.param)
            return _response
        else:
            return False


#发送请求
class AnalysisResponse(object):

    def __init__(self,_response):
        self.response = _response

    #获取状态码
    @property  #用来调用是当做属性来用  不用添加小括号,不用传参
    def getstatuscode(self):
        _getstatuscode = self.response.status_code
        return _getstatuscode

    #转换为DIC格式
    @property
    def dicResponse(self):
        _dicResponse = self.response.json()
        return _dicResponse

    #获取url
    @property
    def getUrl(self):
        _gerUrl = self.response.url
        return _gerUrl

    #获取cookies
    @property
    def getCookies(self):
        pass


    #获取headers
    @property
    def headers(self):
        pass
