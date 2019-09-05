from Tools.BrowserConfig import BrowserConfig
class Selenium_WebElement():
    def __init__(self):
        self.driver = BrowserConfig().driver

    def Element_id(self,revID):
        Element_id = self.driver.find_element_by_id(revID)
        return Element_id

    def Element_name(self,revName):
        Element_name = self.driver.find_element_by_name(revName)
        return Element_name

    def Element_class(self,revClass):
        Element_class = self.driver.find_element_by_class_name(revClass)
        return Element_class

    def Element_Xpath(self,revXpath):
        Element_Xpath = self.driver.find_element_by_xpath(revXpath)
        return Element_Xpath

    def Element_Text(self,revText):
        Element_Text = self.driver.find_element_by_link_text(revText)
        return Element_Text

    def ELement_xpath(self,revXpath):
        ELement_xpath = self.ELement_xpath(revXpath)
        return ELement_xpath
