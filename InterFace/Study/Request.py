import requests
import json
#get请求连接
# url2 = 'http://192.168.1.156:8030/img/1000/42/tp/tp15524247841287.png'
# #post请求连接
# url = 'http://192.168.1.137:8080/sold/app/login'
# #请求参数
# data = {
#     'code':'111111',
#     'mob':'17800000000',
#     'positionX':'116.480059',
#     'positionY':'39.997195',
#     }
class RunMain(object):
    # def __init__(self,url,method,data=None):
    #     self.res = self.run_main(url,method,data)
    #post请求
    def send_post(self,url,data):
        res = requests.post(url=url,data=data).json()
        return json.dumps(res,indent=2)

    #get请求
    def send_get(self,url,data=None):
        res = requests.get(url=url,data=data)
        return json.dumps(res,indent=2,sort_keys=True)

    def run_main(self,url,method,data=None):
        if  method == 'get':
            res = self.send_get(url)
        else:
            res = self.send_post(url,data)
        return json.loads(res)
# if __name__ == '__main__':
#     run = RunMain(url,'post',data)
#     print(run.run_main(url,'post',data))
