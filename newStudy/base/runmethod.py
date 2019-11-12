#coding:utf-8
import requests
import json
class RunMethod:
	def post_main(self,url,data,header=None):
		res = None
		if header != "no":
			res = requests.post(url=url,data=data,headers=header)
		else:
			res = requests.post(url=url,data=data)
			# print("网络请求状态码为："+res.status_code)
		# return res.json()
		if res.status_code == 200:
			return res.json()
		else:
			return "请求地址不存在!,错误状态码为：%s" %res.status_code
	def get_main(self,url,data=None,header=None):
		res = None
		if header !="no":
			res = requests.get(url=url,data=data,headers=header,verify=False)
		else:
			res = requests.get(url=url,data=data,verify=False)
		# return res.json()
		if res.status_code == 200:
			return res.json()
		else:
			return "请求地址不存在!,错误状态码为：%s" %res.status_code
#运行的方法入口
	def run_main(self,method,url,data=None,header=None):
		res = None
		if method == 'post':
			res = self.post_main(url,data,header)
		else:
			res = self.get_main(url,data,header)
		# json.dumps()用于将字典形式的数据转化为字符串，json.loads()用于将字符串形式的数据转化为字典
		# return json.dumps(res,ensure_ascii=False)
		return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)
#
# if __name__ == '__main__':
# 	run = RunMethod()
# 	re = run.run_main('post',"http://192.168.1.156:7091/sold/app/getcode",{"mob":"17800000000"})
# 	print(re)