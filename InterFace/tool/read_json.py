import json
# fp = open('D:/python/Lsm/InterFace/data/json_data.txt')
# data = json.load(fp)
# print(data)
class read_json:
    def __init__(self):
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open("D:/python/Lsm/InterFace/data/json_data.txt") as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,id):
        return self.data[id]

# if __name__ == '__main__':
#     opjson = read_json()
#     print(opjson.get_data('login'))