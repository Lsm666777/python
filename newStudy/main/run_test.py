from newStudy.base.runmethod import RunMethod
from newStudy.data.get_data import GetData
from newStudy.util.common_util import CommonUtil
from newStudy.data.dependent_data import DependdentData
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()

    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rows_count = self.data.get_case_lines()     #调用获取excel行数
        for i in range(1,3):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = str(self.data.get_request_url(i))
                method = self.data.get_request_method(i)
                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                if depend_case != None:
                    self.depend_data = DependdentData(depend_case)
                    #获取的依赖响应数据
                    depend_respinse_data = self.depend_data.get_data_for_key(i)
                    #获取的依赖请求的key值
                    depend_key = self.data.get_depend_field(i)
                    #把上个接口获取的依赖值赋给下个接口
                    request_data[depend_key] = depend_respinse_data
                    #请求接口   method,url,data=None,header=None
                res = self.run_method.run_main(method,url,request_data,header)
                #对比预期结果
                if self.com_util.is_contain(expect,res):
                    #执行结果写进excel
                    self.data.write_result(i,'pass')
                    pass_count.append(i)
                else:
                    #如果不通过，把接口返回信息打印到excel
                    self.data.write_result(i,res)
                    fail_count.append(i)
        #统计case通过与失败数量
        print(len(pass_count))
        print(len(fail_count))
if __name__ == '__main__':
    print(RunTest().go_on_run())
