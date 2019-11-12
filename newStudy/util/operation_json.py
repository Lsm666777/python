
import json
class OperetionJson:

	def __init__(self,file_path=None):
		if file_path  == None:
			# self.file_path = '../dataconfig/user.json'
			self.file_path = 'D:/python/Lsm/newStudy/dataconfig/json_data.json'
		else:
			self.file_path = file_path
		self.data = self.read_data()

	#读取json文件
	def read_data(self):
		with open(self.file_path,encoding='utf-8') as fp:
			data = json.load(fp)
			return data

	#根据关键字获取数据
	def get_data(self,id):
		print (type(self.data))
		return self.data[id]

	#写json
	def write_data(self,data):
		with open('../dataconfig/cookie.json','w') as fp:
			fp.write(json.dumps(data))

if __name__ == '__main__':
	opjson = OperetionJson()
	print (opjson.get_data('mob'))
	# print(opjson.read_data())