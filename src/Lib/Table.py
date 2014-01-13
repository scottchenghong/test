# -*- coding:utf-8 -*-
'''
Created on 2013-11-5

@author: Cliu
'''

#from WebBase import WebBase
# from selenium import webdriver
#from selenium.webdriver.common import by
from web_control import webControl

class  Table(webControl):
    """
    table class
    """
    
    def getCellText(self,xpath='//table[@class="table_data"]//tr'):
        """
        get the Cell Text by the cell row cell
        """
        
        self.data=[]
        
        for tr in self.driver.find_elements_by_xpath(xpath):
            tds=tr.find_elements_by_tag_name('td')
            if tds: 
                #self.data.append([td.text for td in tds])
                
                tdTexts = []
                for td in tds:
                    if td.text != "[详细]":
                        tdTexts.append(td.text)
                self.data.append(tdTexts)
        return self.data[1:]
    
    def getOneCellText(self,channelName,xpath='//table[@class="table_data"]//tr'):
        
        
        tdTexts = []
        for tr in self.driver.find_elements_by_xpath(xpath):
            tds=tr.find_elements_by_tag_name('td')
            if tds[0].text == channelName:
                for td in tds:
                    if td.text != "[详细]":
                        tdTexts.append(td.text)
                break
        return tdTexts
    

if __name__ == "__main__":
    pass