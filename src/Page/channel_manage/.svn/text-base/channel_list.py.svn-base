# -*- coding:utf8 -*-
'''
Created on 2013-8-16

@author: chenghong
'''

from Lib.web_control import webControl


class Channel_list(webControl):
    '''
    进入渠道列表，对渠道进行修改、审核、删除等功能操作
    '''
    
    def add_new_channel(self):
        '''
        点击添加渠道按钮
        '''
        self.click_button("//img[@src = '/yunguan/static/images/operate_button1.jpg']")
        
    def search_channel(self,value):
        '''
        渠道搜索文本框
        @param value:输入要搜索的渠道名称 
        '''
        self.input_textbox('name', value)
        
    def channel_table(self):
        '''
        展示正式渠道列表
        '''
        self.get_xpath("//table[@class = 'table_data']")
        
    def channel_operate(self,channel_name,typecode):
        '''
        渠道的相关操作，包括配置、修改、暂停;
        @param channel_name:要操作的应用名称；
        @param typecode:操作类型，0配置，1修改，2暂停；  
        '''
        if typecode == 0:
            type = '配置'
        elif typecode == 1:
            type = '修改'
        elif typecode == 2:
            type = '暂停'
        else:
            return False
        xpath = "//td[text()='"+channel_name+"']/./following-sibling::td/div/a[text()='"+type+"']"
        self.get_xpath(xpath).click()