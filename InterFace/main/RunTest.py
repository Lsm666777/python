from InterFace.Study.runmethod import RunMethod
from InterFace.data.get_data import GetData
from InterFace.tool.CommonUtil import CommonUtil
from InterFace.data.dependent_data import DependentData
class RunTest:
    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.depend_data = DependentData()
    #程序执行
    def go_on_run(self):
        res = None
        rows_count = self.data.get_case_lines()
        for i in range(1,rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)

                request_data = self.data.get_data_for_json(i)
                expect = self.data.get_expcet_data(i)
                # print('value:'+expect)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)

                # if is_run:
                #     res = self.run_method.run_main(method,url,data,header)
                # return res
                if depend_case != None:
                    #获取以来的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    request_data[depend_key] = depend_response_data
                res = self.run_method.run_main(method,url,request_data,header)


                if self.com_util.is_contain(expect,res):
                    self.data.write_result(i,'pass')
                    # print("测试通过！")
                else:
                    self.data.write_result(i,'fail')
                    # print("测试失败！")

if __name__ == '__main__':
    run = RunTest()
    print(run.go_on_run())
