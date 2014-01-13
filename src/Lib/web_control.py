# -*- coding:utf-8 -*-

'''
Created on Jun 25, 2013

@author: chenghong
'''

from WebBase import WebBase


class webControl(WebBase):
    '''
    页面各类控件
    '''
    
    def input_textbox(self,name,value):
        '''
                 定位文本输入框元素
        '''
        self.driver.find_element_by_name(name).send_keys(value)
        
    def searchButton(self):
        '''
        点击查询按钮
        '''
        self.click_button('//input[@id="searchBtn"]')
        
 
    def click_button(self,xpath):
        '''
                定位按钮元素
        '''
        self.driver.find_element_by_xpath(xpath).click()
    
    def get_drop_down_box(self,attribute,value,text):
        '''
        选择下拉框中的值
        @param attribute: 标签属性
        @param value:属性对应的值
        @param text:该标签对应的text  
        '''
        self.driver.find_element_by_xpath('//select[@%s="%s"]/option[text()="%s"]' %(attribute,value,text)).click()
        
        
    def appear_alert(self):
        '''
                定位警告框，并打印警告信息
        '''
        self.driver.switch_to_alert().text
        
    def skip_frame(self,name):
        '''
                跳转frame
        '''
        self.driver.switch_to_frame(name)
        
    def default_content(self):
        '''
        识别的主体切换出当前frame
        '''
        self.driver.switch_to_default_content() 
    
    def get_xpath(self,xpath):
        '''
        使用xpath定位
        '''
        return self.driver.find_element_by_xpath(xpath)
        
    def getJs(self,js):
        '''
        调用js
        '''
        self.driver.execute_script(js)
        
    def getDatePicker(self,value,datetime):
        '''
        调用日期控件
        '''
        #调用js方法
        js = "dateTime = document.getElementById('%s');\
        dateTime.removeAttribute('readonly');\
        dateTime.setAttribute('value','%s');" % (value,datetime)
        self.getJs(js)
        
    def inputBeginDate(self,datetime):
        '''
        输入开始时间
        '''
        self.getDatePicker('beginDate', datetime)
        
    def inputEndDate(self,datetime):
        '''
        输入结束时间
        '''
        self.getDatePicker('endDate', datetime)