#coding:utf-8
import xlrd
from xlutils.copy import copy
class OperationExcel:
	def __init__(self,file_name=None,sheet_id=None):
		if file_name:
			self.file_name = file_name
			self.sheet_id = sheet_id
		else:
			# self.file_name = '../dataconfig/case1.xls'
			self.file_name = 'D:/python/Lsm/newStudy/dataconfig/data.xls'
			self.sheet_id = 0
		self.data = self.get_data()

	#获取sheets的内容
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheets()[self.sheet_id]
		return tables

	#获取单元格的行数
	def get_lines(self):
		tables = self.data
		return tables.nrows

	#获取某一个单元格的内容
	def get_cell_value(self,row,col):
		return self.data.cell_value(row,col)

	#写入数据
	def write_value(self,row,col,value):
		'''
		写入excel数据
		row,col,value
		'''
		read_data = xlrd.open_workbook(self.file_name)	#打开数据文件
		write_data = copy(read_data)	#复制内容到缓存池
		sheet_data = write_data.get_sheet(0)	#获取当前页所有数据到缓存池
		sheet_data.write(row,col,value)		#插入数据到缓存池
		write_data.save(self.file_name)		#把数据重新保存到excel中

	#根据对应的caseid 找到对应行的内容
	def get_rows_data(self,case_id):
		row_num = self.get_row_num(case_id)	#根据case_id获取到行号
		rows_data = self.get_row_values(row_num)	#根据行号获取到内容
		return rows_data

	#根据对应的caseid找到对应的行号
	def get_row_num(self,case_id):
		num = 0
		clols_data = self.get_cols_data()	#获取当前列的内容
		for col_data in clols_data:
			if case_id in col_data:		#判断寻找case_id
				return num
			num = num + 1

	#根据行号，找到该行的内容
	def get_row_values(self,row):
		tables = self.data
		row_data = tables.row_values(row)	#拿到行的内容
		return row_data

	#获取某一列的内容
	def get_cols_data(self,col_id=None):
		if col_id != None:
			cols = self.data.col_values(col_id)   #获取某一列的内容
		else:
			cols = self.data.col_values(0)
		return cols


if __name__ == '__main__':
	opers = OperationExcel()
	print (opers.get_cell_value(1,2),type(opers.get_cell_value(1,2)))
	# print (opers.get_lines())