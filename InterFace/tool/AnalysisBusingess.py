from InterFace.tool.GetRessponse import GetRessponse
from InterFace.tool.GetRessponse import AnalysisResponse
class AnalysisBusingess(object):
    def analysisResponse(self,_url,_param=None,_method='get'):
        _rvResponse = GetRessponse(_url=_url, _param=None,_method='get').getResponse()
        _rvAnalsisResponse = AnalysisResponse(_rvResponse)
        return _rvAnalsisResponse
    #验证服务器返回http状态码
    def assertStatusCode(self,_url,_param,_exp):
        _actStatusCode = self.analysisResponse(_url,_param,_exp).getstatuscode
        assert _actStatusCode == _exp,"状态码对比失败"

    #验证服务器响应状态码返回200
    def assertResultcode(self,_url,_param,_exp,_method='post'):
        _assertResultcode = self.analysisResponse(_url,_param,_exp,_method='post').dicResponse
        _actResulcode = _assertResultcode['result']['code']
        print(_actResulcode)
        assert _actResulcode == _exp, "['result']['code']对比失败"

    #验证服务器响应返回resultMessage