import os
import sys
os.getcwd()
sys.path.append(os.getcwd())
from xml.dom import minidom
import xlrd
class PythonHelpApi(object):
    # def ReadXmlData(self,fileName,firstTag,SecondTag):
    #     a="/Users/newroad/PycharmProjects/TinyShopAutoTestProject/TinyShopDataPool/XmlData/"
    #     XmlName=minidom.parse(a+fileName+'.xml')
    #     OneTag=XmlName.getElementsByTagName(firstTag)[0]
    #     TwoNodeValue=OneTag.getElementsByTagName(SecondTag)[0].childNodes[0].nodeValue
    #     return TwoNodeValue
    def ReadExcelData(self,SheetName,x,y):
        #b="/Users/newroad/PycharmProjects/TinyShopAutoTestProject/TinyShopDataPool/ExcelData/Web_Element.xlsx"
        c = "C:\\Users\\14684\\PycharmProjects\\webcase1\\DataSeparation\\ExcelData\\UntestCase.xlsx"
        ExcelName=xlrd.open_workbook(c)
        CallValue=ExcelName.sheet_by_name(SheetName).cell_value(x,y)
        return CallValue
