# -*- coding:utf8 -*-
'''
Created on 2013-7-22

@author: chenghong
'''
import time
from selenium import webdriver
from Lib.web_control import webControl
from Page.login import Login
from Page.left_menu import Left_menu

class New_channel(webControl):
    '''
    用户登陆后，点击“新增渠道”,跳转到渠道新建页面
    '''
    def channel_frame(self):
        '''
        切换到‘渠道新建’页面
        '''
        self.skip_frame('mainFrame')
        self.skip_frame('I2')
        
    def search_channel(self,value):
        '''
        在‘渠道名称’文本框输入渠道即value值
        '''
        self.input_textbox('name', value)
        
    def click_search_button(self):
        '''
        点击渠道查询按钮
        '''
        self.click_button("//img[@onclick = 'search()']")
        
    def add_new_channel(self):
        '''
        点击添加渠道按钮
        '''
        self.click_button("//img[@src = '/yunguan/static/images/operate_button1.jpg']")
        
    def open_channel_table(self):
        '''
        展示临时渠道表单
        '''
        return self.get_xpath("//table[@class = 'table_data']").text
    
    def new_channel_operate(self,channel_name,typecode):
        '''
        新建渠道的相关操作，包括修改、删除、审核
        @param channel_name:要操作的应用名称；
        @param typecode:操作类型，0审核，1修改，2删除；  
        '''
        if typecode == 0:
            type = '审批'
        elif typecode == 1:
            type = '修改'
        elif typecode == 2:
            type = '删除'
        else:
            return False
        xpath = "//td[text()='"+channel_name+"']/./following-sibling::td/div/a[text()='"+type+"']"
        self.get_xpath(xpath).click()
    
if __name__ == '__main__':
    
    #赋值参数
    url = 'http://192.168.188.201/yunguan/login'
    driver = webdriver.Firefox()
    
    #实例化对象
    User_login = Login(driver,url)
    Menu = Left_menu(driver,url)
    channel = New_channel(driver,url)
    
    try:
        #用户登陆
        User_login.input_usr('admin')
        User_login.input_pwd('admin')
        User_login.click_confirm_button()
        
        #跳转页面到left_menu
        Menu.skip_left_frame()
        
        #用户点击应用管理按钮
        Menu.manage_channel()
        time.sleep(2)
        Menu.add_new_channel()
        time.sleep(2)
        
        #跳转页面
        channel.default_content()
        channel.channel_frame()
        print 'move frame ok'
        
        #输入查询的channelname
        channel.search_channel(u'河北保定电信')
        time.sleep(2)
        #点击查询
        channel.click_search_button()
        time.sleep(2)
        print channel.open_channel_table()
        time.sleep(2)
    except Exception as e:
        print e
    finally:
        Menu.close()