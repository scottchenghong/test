#coding:utf8
'''
Created on 2013-11-13

@author: chenghong
'''
import time
import unittest
from selenium import webdriver
from Page.left_menu import Left_menu
from Page.report_manage.interiorPushMoneyTotalReport import InteriorPushMoneyTotalReport
from Lib.Table import Table
from Lib import pagewait
import TestPremiseCaseLogin as login
from Page.topframe import TopFrame


class TestInteriorPushMoneyTotalReport(unittest.TestCase):
    '''
    测试商务人员提成报表
    '''
    def setUp(self):
        '''
        初始化登陆操作
        '''
        self.user = 'admin'
        self.pwd= 'cdsf_2012'
        self.url = 'http://192.168.188.201/yunguan/login'
        self.driver = webdriver.Firefox()
        
        self.Menu = Left_menu(self.driver,self.url)
        self.interior = InteriorPushMoneyTotalReport(self.driver,self.url)
        self.Table = Table(self.driver,self.url)
        self.TopFrame = TopFrame(self.driver,self.url)
        
        try:
            #admin用户登陆后台
            login.getUserLogin(self.driver, self.url, self.user, self.pwd)
            
            pagewait.waitPage(self.driver,'//frame[@id="mainFrame"]','login failed')
            
            #页面跳转至左边菜单栏,依次点击'报表管理'、'商务人员提成报表'
            self.Menu.switch_left_frame()
#             pagewait.waitPage(self.driver, xpath, msg)
            self.Menu.open_report_manage()
            time.sleep(1)
            pagewait.waitPage(self.driver,'//a[text()="商务人员提成报表"]', 'open reportManage failed')
            #点击'商务人员报表'
            self.Menu.getInteriorPushMoneyTotalReport()
            
            #退出左边frame,进入报表主页面
            self.Menu.default_content()
            self.Menu.switchMainFrame()
        except Exception as e:
            return e
            
    def testinterior(self):
        
        '''
        测试商务人员进行查询，且比较页面的提成金额与详细页面的各个应用包提成金额之和是否一致
        '''
        
        try:
            #输入商务人员名称
            self.interior.inputUserName(u'丁迪')
            #点击查询按钮
            self.interior.searchButton()
            #获取页面表单查询内容
            allData = self.Table.getCellText()
            #统计提成金额
            for money in allData:
                totalmoney = float(money[1])
#                 print totalmoney
                
            #点击详细按钮
            self.interior.clickDetailButton('丁迪')
            
            sum = 0
            #进入详细页面，计算商务人员每个应用包的提成之和
            for money in self.Table.getCellText():
                sum += float(money[-1])
#             print sum
                    
            #断言。判断是否有数据
            self.assertTrue(allData, 'data is null')
            self.assertEqual(totalmoney, sum, '提成金额不一致')
        except Exception as e:
            return e
        
    def testDateTime(self):
        
        '''
        根据时间段进行查询，验证日期段查询功能是否有效
        '''
        
        try:
            #输入开始时间
            self.interior.inputBeginDate('2013-10-01')
            #输入结束时间
            self.interior.inputEndDate('2013-10-31')
            #点击查询按钮
            self.interior.searchButton()
            
            #获取页面表单查询内容
            allData = self.Table.getCellText()
            
            #断言
            self.assertTrue(allData, 'data is null')
        except Exception as e:
            return e
        
    def testInteriorSelfPush(self):
        '''
        商务人员登陆只能看到自己的提成
        '''
        
        try:
            #点击退出登陆，切换商务人员账号进行登陆
            self.Menu.default_content()
            self.TopFrame.switchTopFrame()
            
            pagewait.waitPage(self.driver,"//img[@src='/yunguan/static/images/top_photo3.jpg']", 'switch topframe failed')
            
            self.TopFrame.loginOut()
            
            pagewait.waitPage(self.driver,'//div[@id="login"]', 'login out failed')
            #商务人员用户登陆后台
            login.getUserLogin(self.driver, self.url, 'liuxinrui', 'cdsf_2012')
            
            pagewait.waitPage(self.driver,'//frame[@id="mainFrame"]','login failed')
            
            #页面跳转至左边菜单栏,依次点击'报表管理'、'商务人员提成报表'
            self.Menu.switch_left_frame()
            self.Menu.open_report_manage()
            time.sleep(1)
            pagewait.waitPage(self.driver,'//a[text()="商务人员提成报表"]', 'open reportManage failed')
            #点击'商务人员报表'
            self.Menu.getInteriorPushMoneyTotalReport()
            
            #退出左边frame,进入报表主页面
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            
            #统计页面佣金数据
            pageData = self.Table.getCellText()
            for pageMoney in pageData:
                money = float(pageMoney[1])
#                 print money
                
            #点击详细，并统计各应用包提成之和
            self.interior.clickDetailButton(pageMoney[0])
            
            sum = 0
            for totalMoney in self.Table.getCellText():
                sum += float(totalMoney[-1])
#             print sum
            
            #断言，比较money与totalMoney的值是否一致
            self.assertEqual(money, sum, 'money is not equal')
        except Exception as e:
            return e
    
    
    def tearDown(self):
        self.driver.close()
        
if __name__ == '__main__':
    unittest.main()
            