# coding:utf8

'''
Created on 2013-11-20

@author: chenghong
'''

import time
import unittest
from selenium import webdriver
from Lib.Table import Table
from Lib import pagewait
from Page.left_menu import Left_menu
from Page.app_manage.mmAppList import MMAppList
from TestCase import TestPremiseCaseLogin as login


class TestmmAppList(unittest.TestCase):
    '''
    测试"移动渠道应用获取"功能，主要测试查询、下载操作，下载后的"未下载"状态变为"下载"
    '''
    
    def setUp(self):
        '''
        初始化用户登录
        '''
        self.driver = webdriver.Firefox()
        self.url = 'http://192.168.188.201/yunguan/login'
        self.user = 'admin'
        self.pwd = 'cdsf_2012'
        
        self.menu = Left_menu(self.driver,self.url)
        self.mm = MMAppList(self.driver,self.url)
        self.table = Table(self.driver,self.url)
        
        try:
            #用户登陆
            login.getUserLogin(self.driver, self.url, self.user, self.pwd)
            
            pagewait.waitPage(self.driver,'//frame[@id="mainFrame"]','login failed')
            #进入左边菜单，点击应用管理
            self.menu.switch_left_frame()
            self.menu.click_app_manege()
            
            time.sleep(1)
            pagewait.waitPage(self.driver,'//a[@id="mmappList"]', 'open appManage failed')
            
            #点击"移动渠道应用获取"
            self.mm.clickMMAppList()
            self.menu.default_content()
            self.menu.switchMainFrame()
            
            pagewait.waitPage(self.driver, '//input[@id="name"]','loading mainframe failed')
            
        except Exception as e:
            return e
    def testMMAppList(self):
        '''
        测试业务流程：查询和下载操作
        '''
        try:
            #获取页面表单数据,并取得第一行应用名称
            appList = self.table.getCellText()
#             print appList[0][0]
                
            #输入应用名称 ,点击查询按钮
            self.mm.inputAppName(appList[0][0])
            self.mm.clickSearchButton()
             
            for app in self.table.getCellText():
                appname = app[0]
#                 print appname
                
            #断言。查询结果显示的appname与查询输入的app对比一致性
            self.assertEqual(appname, appList[0][0],'data is not equal')
            
            #点击下载操作，统计应用状态变为'已下载'
            self.mm.clickDownLoadApp(appList[0][0])
            for app in self.table.getCellText():
                appStatus = app[-2]
#                 print appStatus
                
            #断言。检查app status是否是'已下载'
            self.assertEqual(appStatus,'已下载', 'download unresponsive')
        except Exception as e:
            return e
        
    def tearDown(self):
        self.driver.close()
        
        
if __name__ == '__main__':
    unittest.main()