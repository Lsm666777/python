def CreatHTMLTestReport(self, fileName, rev_T, RevD, rev_Test):
    #  通过相对路径找到测试报告，因通用模块文件名不能写死变量接受

    File1 = '/Users/poptest/PycharmProjects/WebTinyshop/TestReport/' + fileName + '.html'

    # 使用with open 打开测试报告模版并以二进制的形式卸乳具体测试报告内容
    # 并保存到内存空间W代表写 b 代表二进制 as 代表存储
    with open(File1, 'wb') as HTMLstream:
        # 使用HTML生成具体内容
        HTMLTestRunner.HTMLTestRunner(
            # 文本流向  内存空间
            stream=HTMLstream,
            # 报告详细级别，一般使用1或2 ，当使用多条用例执结果不同只会
            # 返回唯一结果且有限顺序是error>fail>pass
            verbosity=2,
            # 测试标题，通用模块标题名不能写死变量接收
            title=rev_T,
            # 测试用例具体描述信息，通用模块不能写死，变量接收
            description=RevD
            #     运行具体用例生成测试报告
        ).run(rev_Test)