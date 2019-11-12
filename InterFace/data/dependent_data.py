
from InterFace.tool.read_excel import OperationExcel
from InterFace.Study.runmethod import RunMethod
from InterFace.data.get_data import GetData
from jsonpath_rw import jsonpath,parse
class DependentData:
    def __init__(self,case_id):
        self.opera_excel = OperationExcel()
        self.case_id = case_id
        self.run_method = RunMethod()
        self.data = GetData()

    #通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    #执行依赖测试，获取结果
    def run_dependent(self):
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        header = self.data.is_header(row_num)
        method = self.data.get_request_method(row_num)
        url = self.data.get_request_url(row_num)
        res = self.run_method.run_main(method,url,request_data,header)
        return res

    #根据依赖的key去获取执行一来测试case的相应，然后返回
    def get_data_for_key(self,row):
        depend_data = self.data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data)
        '''  
        for i in madle:
            print(i.value)
        '''
        # 这是一个for循环，普通for循环的简写
        return [math.value for math in madle][0]




