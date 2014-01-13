# -*- coding:utf-8 -*-
'''
Created on 2013-7-11
@author:Liu Chengshuang 
'''
from selenium import webdriver
from Lib.web_control import webControl
from Page.left_menu import Left_menu
from Page.login import Login
import time
from Page.app_manage.appList import AppList


class AppInfoModify(webControl):
    '''
    应用信息修改page类，由应用列表--应用--修改跳转而来
    '''
    
    def ModifyAppName(self,NewAppName):
        '''
        @summary: 修改应用该名称
        @param NewAppName:新的app名称
        '''
        self.input_textbox("app_name", NewAppName)
    
    def ModifyAppBnsUser(self,NewBnsUser):
        
        '''
        @param NewBnsUser:新的应用负责人
        @summary:选择新的应用负责人
        '''
        self.select_drop_down_box('bns_user', NewBnsUser)
    
    def ModifyAppCP(self,NewCP):
        '''
        @param NewCP:新的CP名称
        @summary: 修改该应用的CP信息
        '''
        self.get_xpath("//select[@name='cp_ap_id']").find_elements_by_tag_name('option')[2].click()
        #self.select_drop_down_box('cp_ap_id', NewCP)
    
    def ModifyAppPrice(self,NewPrice):
        '''
        @param NewPrice: 新的应用单价
        @summary:修改应用单价信息
        '''
        self.input_textbox('app_price', NewPrice)
        
    def ModifyAppCycle(self,NewCycle):
        '''
        @param NewCycle: 新的结算周期
        @summary: 修改应用结算周期
        '''
        self.select_drop_down_box('app_cycle', NewCycle)
        
    def ModidyAppChannelCond(self,NewCond):
        '''
        @param NewCond: 新的应用引入特殊需求
        @summary: 修改应用应用特殊需求
        '''
        self.input_textbox('channel_cond', NewCond)
        
    def ModidyAppActivateType(self,NewActivateType):
        '''
        @param NewActivateType: 新的激活类型
        @summary: 修改应用激活类型
        '''
        self.input_textbox('activate_type', NewActivateType)
        
    def ModifyAppActiveInterval(self,NewInterval):
        '''
        @param NewInterval: 新的激活间隔时间
        @summary: 修改应用首次激活与二次激活间隔时间
        '''
        self.input_textbox('active_hour', NewInterval)
    
    def ModifyAppActivateLastDay(self,NewLastDay):
        '''
        @param NewLastDay: 新的后续激活上报时限
        @summary:修改后续激活上报时限
        '''
        self.input_textbox('active_day',NewLastDay)
    
    def Commit(self):
        '''
        @summary: 点击提交按钮
        '''
        self.click_button("//input[@id='_add_app']")
        
    def Cancel(self):
        '''
        @summary: 取消提交
        '''
        self.click_button("//input[@type='reset']")
        
        

if __name__ == '__main__':
    
    driver = webdriver.Firefox()
    url = 'http://192.168.188.201/yunguan/login'
    
    User_login = Login(driver,url)
    Menu = Left_menu(driver,url)
    applist = AppList(driver,url)
    modifypage = AppInfoModify(driver,url)
    
    try:
        User_login.input_usr('admin')
        User_login.input_pwd('admin')
        User_login.click_confirm_button()
        Menu.skip_left_frame()
        Menu.click_app_manege()
        time.sleep(2)
        Menu.open_app_list()
        applist.default_content()
        applist.app_iframe()
        appname = u"百度搜索"
        
        applist.AppListOperate(appname,1)
        modifypage.ModifyAppCP('CP')
        #modifypage.ModifyAppBnsUser('张荣')
        #modifypage.ModifyAppCycle('一周')
        modifypage.Commit()
        
        time.sleep(10)
    except Exception as e:
        print e
    finally:
        applist.close()
