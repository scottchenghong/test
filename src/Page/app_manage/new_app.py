# -*- coding:utf-8 -*-
'''
Created on Jul 10, 2013

@author: chenghong
'''

import time
from selenium import webdriver
from Page.left_menu import Left_menu
from Page.login import Login
from Lib.web_control import webControl

class New_app(webControl):
    '''
    该page是用户点击“新增应用”按钮后，跳转到应用新增页面；
    页面功能包括应用查询、新增应用、临时应用展示（从yg_app_info表获取）
    '''
    def app_iframe(self):
        '''
        跳转至新增应用iframe页面
        '''
        self.skip_frame('mainFrame')
        self.skip_frame('I2')
        
    def select_app(self,value):
        '''
        输入应用名称，查询目前应用，支持模糊查询
        '''
        self.input_textbox('name', value)
        
    def click_search_button(self):
        '''
        点击查询按钮
        '''
        self.click_button("//img[@id='_appSearch']")
        
    def add_new_app(self):
        '''
        点击’添加应用按钮‘
        '''
        self.click_button("//img[@src='/yunguan/static/images/operate_button1.jpg']")
        
    def open_app_table(self):
        '''
        展示所有临时应用
        '''
        return self.get_xpath("//table[@class='table_data']").text
    
if __name__ == '__main__':
    '''
    '''
    #赋值参数
    url = 'http://192.168.188.201/yunguan/login'
    driver = webdriver.Firefox()
    
    #实例化对象
    User_login = Login(driver,url)
    Menu = Left_menu(driver,url)
    app = New_app(driver,url)
    
    try:
        #用户登陆
        User_login.input_usr('admin')
        User_login.input_pwd('cdsf_2012')
        User_login.click_confirm_button()
        
        #跳转页面到left_menu
        Menu.skip_left_frame()
        
        #用户点击应用管理按钮
        Menu.click_app_manege()
        time.sleep(2)
        Menu.add_new_app()
        time.sleep(2)
        
        #跳转页面
        app.default_content()
        app.app_iframe()
        print 'move frame ok'
        
        #输入查询的appname
        app.select_app(u'百度')
        time.sleep(2)
        #点击查询
        app.click_search_button()
        time.sleep(2)
        print app.open_app_table()
    except Exception as e:
        print e
    finally:
        Menu.close()
    