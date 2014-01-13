# -*- coding:utf-8 -*-
'''
Created on Jul 8, 2013

@author: chenghong
'''
import time
from selenium import webdriver
from Lib.web_control import webControl
from Page.login import Login

class Left_menu(webControl):
    '''
    封装index页面左边菜单栏的功能按钮
    '''
    def switch_left_frame(self):
        '''
        跳转页面到left_menu
        '''
        self.skip_frame('mainFrame')
        self.skip_frame('I1')
        
    def switchMainFrame(self):
        '''
        点击左边功能图标后，跳转页面到右边对应功能主页面
        '''
        self.skip_frame('mainFrame')
        self.skip_frame('I2')
        
    def click_app_manege(self):
        '''
        应用管理按钮
        '''
        #应用管理
        
        self.click_button("//img[@src='/yunguan/static/images/left_title5.jpg']")
        
    def add_new_app(self):
        '''
        应用管理列表下的新增应用
        '''
        self.click_button("//a[@id='getAppList']")
        
    def open_app_list(self):
        '''
        应用管理列表下的应用列表
        '''
        self.click_button("//a[@id='getOffAppList']")
        
    def manage_channel(self):
        '''
        渠道管理按钮
        '''
        self.click_button("//img[@src='/yunguan/static/images/left_title2.jpg']")
    
    def add_new_channel(self):
        '''
        新增渠道按钮
        '''
        self.click_button("//a[@id='getChannel']")
        
    def open_channel_list(self):
        '''
        渠道列表
        '''
        self.click_button("//a[@id='getOffChannel']")
        
    def click_bill_manage(self):
        '''
        对账管理
        '''
        self.click_button("//img[@src='/yunguan/static/images/left_title3.jpg']")
        
    def open_accountList(self):
        '''
        日激活量
        '''
        self.click_button("//a[@href='/yunguan/balance/accountList']")
        
    def click_system_manage(self):
        '''
        系统管理
        '''
        self.click_button("//img[@src='/yunguan/static/images/left_title1.jpg']")
        
    def open_user_list(self):
        '''
        用户列表
        '''
        self.click_button("//a[@href='/yunguan/userIndex']")
        
    def open_role_list(self):
        '''
        角色列表
        '''
        self.click_button("//a[@href='/yunguan/roleList']")
        
    def open_report_manage(self):
        '''
        报表管理
        '''
        self.click_button("//img[@src='/yunguan/static/images/left_title4.jpg']")
        
    def get_total_report(self):
        '''
        总盘报表
        '''
        self.click_button("//a[@href='/yunguan/report/totalReport']")
        
    def get_app_report(self):
        '''
        应用维度数据统计报表
        '''
        self.click_button("//a[@href='/yunguan/report/applicationDimensionReport']")
        
    def get_channel_app_report(self):
        '''
        渠道应用报表
        '''
        self.click_button("//a[@href='/yunguan/report/appAngleReport/day']")
        
    def get_channel_level_report(self):
        '''
        渠道层级报表
        '''
        self.click_button("//a[@href='/yunguan/report/channelLevelReport']")
        
    def clickListDeviceNetwork(self):
        '''
        点击联网通报报表
        '''
        self.click_button("//a[@href='/yunguan/report/listDeviceNetwork']")
    
    def getChannelFluxReport(self):
        '''
        渠道流量报表
        '''
        self.click_button('//a[@href="/yunguan/report/channelFluxReport_new"]')
        
    def getChannelLevelReport(self):
        '''
        渠道报表
        '''
        self.click_button('//a[@href="/yunguan/report/channelLevelReport"]')
        
    def getAppAngleReport(self):
        '''
        渠道应用报表
        '''
        self.click_button('//a[@href="/yunguan/report/appAngleReport/day"]')
        
    def getSixClockReport(self):
        '''
        六点报表
        '''
        self.click_button('//a[@href="/yunguan/report/sixoClockReport"]')
        
    def getListBulletinDayReport(self):
        '''
        通报日报报表
        '''
        self.click_button('//a[@href="/yunguan/report/listBulletinReport?type=Day"]')
        
    def getListBulletinWeekReport(self):
        '''
        通报周报报表
        '''
        self.click_button('//a[@href="/yunguan/report/listBulletinReport?type=Week"]')
        
    def getInteriorPushMoneyTotalReport(self):
        '''
        商务人员提成报表
        '''
        self.click_button('//a[text()="商务人员提成报表"]')
        
        
        
if __name__ == '__main__':
    '''
    调试封装方法：
    包括用户登陆，访问左边菜单每个功能
    '''
    
    #赋值参数
    url = 'http://192.168.188.201/yunguan/login'
    driver = webdriver.Firefox()
    
    #实例化对象
    User_login = Login(driver,url)
    Menu = Left_menu(driver,url)
    
    try:
        #用户登陆
        User_login.input_usr('admin')
        User_login.input_pwd('admin')
        User_login.click_confirm_button()
        
        #跳转页面到left_menu
        Menu.skip_left_frame()
        
        #用户点击应用管理按钮
        Menu.open_report_manage()
        time.sleep(2)
        Menu.click_channel_level_report()
        time.sleep(5)
    except Exception as e:
        print e
    finally:
        Menu.close()
        