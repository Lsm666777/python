from selenium.webdriver.common.action_chains import ActionChains
from Tools.BrowserConfig import BrowserConfig
#封装鼠标机制
class selenium_mouse(object):
    def __init__(self):
        self.driver = BrowserConfig().driver
    #移动鼠标
    def Move_mouse(self,Element):
        ActionChains(self.driver).move_to_element(Element).perform()

    #双击鼠标
    def double_mouse(self,Element):
        ActionChains(self.driver).double_click(Element).perform()

    #鼠标悬停操作
    def Mouse_move_to_element(self,a):
        ActionChains(self.driver).move_to_element(to_element=a).perform()

    #模拟鼠标右击操作
    def contest_click(self,Element):
        ActionChains(self.driver).context_click(Element).perform()  # perform() 可以理解为对整个操作的提交动作。ActionChains(self.driver)类，将浏览器驱动driver作为参数传入

    #鼠标拖放操作
    def aaa(self,origin,destination):
        ActionChains(self.driver).drag_and_drop(source=origin,target=destination).perform()

    # def __init__(self):
    #     self.driver = BrowserConfig().driver

    # def Mouse_click_and_hold(self,On_Element):
    #     ActionChains(self.driver).click_and_hold(On_Element).perform()
    #
    # def Mouse_context_click(self,On_Element):
    #     ActionChains(self.driver).context_click(On_Element).perform()
    #
    # def Mouse_double_click(self,On_Element):
    #     ActionChains(self.driver).double_click(On_Element).perform()
    #
    # def Mouse_drag_and_drop(self,a,b):
    #     ActionChains(self.driver).drag_and_drop(a,b).perform()
    #
    # def Mouse_drag_and_drop_by_offset(self,Element,x,y):
    #     ActionChains(self.driver).drag_and_drop_by_offset(Element,x,y).perform()

    def Mouse_key_down(self,V,element):
        ActionChains(self.driver).key_down(V,element)

    def Mouse_key_up(self,V,element):
        ActionChains(self.driver).key_up(V,element)


    def Mouse_move_to_element_with_offset(self,a,x,y):
        ActionChains(self.driver).move_to_element_with_offset(to_element=a,xoffset=x,yoffset=y).perform()