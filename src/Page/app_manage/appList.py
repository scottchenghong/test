# -*- coding:utf-8 -*-
'''
Created on 2013-7-11
@author:Liu Chengshuang 
'''
from selenium import webdriver
from Lib.web_control import webControl
from Page.left_menu import Left_menu



class AppList(webControl):
    '''
    应用列表页面
    '''
    def app_iframe(self):
        '''
        新增应用、应用列表均会使用到本方法切换iframe
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
    
   
    def AppListOperate(self,appName,TypeCode):
        
        
        '''
        @param appName:应用名称
        @param TypeCode:操作类型代码，0为查看应用包信息，1为修改
        '''
        if TypeCode == 0:
            Type = "查看应用包信息"
        elif TypeCode == 1 :
            Type = "修改"
        else :
            print "错误的操作类型代码"
        
        Xpath = "//td[text()='"+appName+"']/./following-sibling::td/div/a[text()='"+Type+"']"
        print Xpath
        self.get_xpath(Xpath).click().text
    

if __name__ == '__main__':
    
    from Page.login import Login
    import time
    
    driver = webdriver.Firefox()
    url = 'http://192.168.188.201/yunguan/login'
    
    User_login = Login(driver,url)
    Menu = Left_menu(driver,url)
    applist = AppList(driver,url)
    
    try:
        User_login.input_usr('admin')
        User_login.input_pwd('cdsf_2012')
        User_login.click_confirm_button()
        Menu.skip_left_frame()
        Menu.click_app_manege()
        time.sleep(2)
        
        Menu.open_app_list()
        applist.default_content()
        applist.app_iframe()
        
        applist.AppListOperate(u"百度搜索",0)
        time.sleep(3)
    except Exception as e:
        print e
    finally:
        applist.close()
