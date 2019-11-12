import requests
import json
class RunMethod:
    def post_main(self,url,data,headers=None):
        if headers !=None:
            res = requests.post(url=url,data=data,headers=headers).json()
        else:
            res = requests.post(url=url,data=data).json()
        return res

    def get_main(self,url,data=None,headers=None):
        if headers != None:
            res = requests.get(url=url, data=data,headers=headers).json()
        else:
            res = requests.get(url=url, data=data).json()
        return res

    def run_main(self,method,url,data,headers=None):
        if method == 'post'or method == 'POST':
            res = self.post_main(url,data,headers)
        else:
            res = self.get_main(url,data,headers)
        # return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
        return res