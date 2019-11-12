
class global_var():
    Id = '0'
    name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend = '7'
    field_depend = '8'
    data = '9'
    expect = '10'
    result = '11'

        #获取id
    def get_id(self):
        return global_var.Id

        #获取url
    def get_url(self):
        return global_var.url

        #获取run
    def get_run(self):
        return global_var.run

        #获取request
    def get_request_way(self):
        return global_var.request_way

        #获取header
    def get_header(self):
        return global_var.header

        #获取case_depend
    def get_case_depend(self):
        return global_var.case_depend

        #获取data_depend
    def get_data_depend(self):
        return global_var.data_depend

        #获取field_depend
    def get_field_depend(self):
        return global_var.field_depend

        #获取data
    def get_data(self):
        return global_var.data

        #获取expext
    def get_expect(self):
        return global_var.expect

        #获取result

    def get_result(self):
        return global_var.result

    def get_header_value(self):
        header = {
            'header':'1234',
            'cookie':'lsm'
        }
        return header
# if __name__ == '__main__':
#     run = global_var()
#     print(run.get_run())



