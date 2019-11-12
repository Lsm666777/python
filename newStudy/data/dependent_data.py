import sys
import json
from newStudy.util.operation_excel import OperationExcel
from newStudy.base.runmethod import RunMethod
from newStudy.data.get_data import GetData
from jsonpath_rw import jsonpath,parse
from newStudy.util.forkey import GetKeyValue
class DependdentData:
	def __init__(self,case_id):
		self.case_id = case_id
		self.opera_excel = OperationExcel()
		self.data = GetData()
		self.run_method = RunMethod()

	#通过case_id去获取该case_id的整行数据
	def get_case_line_data(self):
		# 根据对应的caseid 找到对应行的内容
		rows_data = self.opera_excel.get_rows_data(self.case_id)
		return rows_data

	#执行依赖测试，获取结果
	def run_dependent(self):

		# 根据对应的caseid找到对应的行号
		row_num  = self.opera_excel.get_row_num(self.case_id)
		# 依赖case获取请求数据
		request_data = self.data.get_data_for_json(row_num)
		#header = self.data.is_header(row_num)
		method = self.data.get_request_method(row_num)
		url = self.data.get_request_url(row_num)
		res = self.run_method.run_main(method,url,request_data)
		return json.loads(res)

		# a = json.loads(res)
		# return a["data"]
		# data = json.loads(res) 	#转成json对象，在python里也就是dict类型
		# return data['data']['storeId']

	#根据依赖的key去获取执行依赖测试case的响应数据,然后返回
	def get_data_for_key(self,row):

		# 获取依赖数据的key 7
		depend_data = self.data.get_depend_key(row)
		# 获取依赖case的结果
		response_data = self.run_dependent()
		# 根据获取依赖数据的key去遍历获取依赖case的结果
		return_data = GetKeyValue(response_data).search_key(depend_data)
		return return_data[0]

		# json_exe = parse(depend_data)
		# madle = json_exe.find(response_data)		#返回是一个列表
		# return [math.value for math in madle][0]
		# for i in madle:
		# 	i.value
if __name__ == '__main__':
	run = DependdentData('login--001')	#传入依赖的caseId
	# print(run.run_dependent())
	print(run.get_data_for_key(2))





















	# order = {
	# 	"data": {
	# 		"_input_charset": "utf-8",
	# 		"body": "慕课网订单-1710141907182334",
	# 		"it_b_pay": "1d",
	# 		"notify_url": "http://order.imooc.com/pay/notifyalipay",
	# 		"out_trade_no": "1710141907182334",
	# 		"partner": "2088002966755334",
	# 		"payment_type": "1",
	# 		"seller_id": "yangyan01@tcl.com",
	# 		"service": "mobile.securitypay.pay",
	# 		"sign": "kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D",
	# 		"sign_type": "RSA",
	# 		"string": "_input_charset=utf-8&body=慕课网订单-1710141907182334&it_b_pay=1d&notify_url=http://order.imooc.com/pay/notifyalipay&out_trade_no=1710141907182334&partner=2088002966755334&payment_type=1&seller_id=yangyan01@tcl.com&service=mobile.securitypay.pay&subject=慕课网订单-1710141907182334&total_fee=299&sign=kZBV53KuiUf5HIrVLBCcBpWDg%2FnzO%2BtyEnBqgVYwwBtDU66Xk8VQUTbVOqDjrNymCupkVhlI%2BkFZq1jOr8C554KsZ7Gk7orC9dDbQlpr%2BaMmdjO30JBgjqjj4mmM%2Flphy9Xwr0Xrv46uSkDKdlQqLDdGAOP7YwOM2dSLyUQX%2Bo4%3D&sign_type=RSA",
	# 		"subject": "慕课网订单-1710141907182334",
	# 		"total_fee": 299
	# 		},
	# 		"errorCode": 1000,
	# 		"errorDesc": "成功",
	# 		"status": 1,
	# 		"timestamp": 1507979239100
	# 	}
	# res = "data.out_trade_no"
	# json_exe = parse(res)
	# madle = json_exe.find(order)
	# print ([math.value for math in madle][0])


