#coding:utf8

'''
Created on 2013-11-11

@author: chenghong
'''

import time,unittest
from selenium import webdriver
from Lib.WebBase import WebBase
from TestCase import TestPremiseCaseLogin as Login
from Page.left_menu import Left_menu
from Lib.Table import Table
from Lib.Mysql import Mysql
from Page.report_manage.channelFluxReport import channelFluxReport
from Page.report_manage.channelResourcesTree import ChannelResourcesTree
from Lib import pagewait

class TestChannelFluxReport(unittest.TestCase,WebBase):
    '''
    渠道流量报表测试用例
    '''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.url = 'http://192.168.188.201/yunguan/login'
        self.user = 'admin'
        self.pwd = 'cdsf_2012'
       
        #实例化对象
        self.Menu = Left_menu(self.driver,self.url)
        self.Mysql = Mysql()
        self.Table = Table(self.driver,self.url)
        self.ChannelFlux = channelFluxReport(self.driver,self.url)
        self.ChannelTree = ChannelResourcesTree(self.driver,self.url)
        
        try:
            #初始化登陆和页面跳转
            
            Login.getUserLogin(self.driver,self.url,self.user,self.pwd) #admin用户登陆
            pagewait.waitPage(self.driver,'//frame[@id="mainFrame"]','login failed')
            time.sleep(3)
        
            #跳转页面
            self.Menu.switch_left_frame()  
            self.Menu.open_report_manage()
        
            time.sleep(1)
            pagewait.waitPage(self.driver,'//a[text()="渠道流量报表"]', 'open reportManage failed')
        
            self.Menu.getChannelFluxReport()
            #跳出原来frame
            self.Menu.default_content() 
            self.Menu.switchMainFrame()
            time.sleep(1)
        except Exception as e:
            raise e
    def estTotalChannelCompareSelfChannel(self):
        '''
    查询数据，比较总渠道页面的自有渠道数据和自有渠道页面的合计当前行数据一致性
        '''
        try:
            #选择总渠道
            self.ChannelTree.getChannel('总渠道')
            time.sleep(1)
            #跳转页面
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            
            #输入时间查询
            self.ChannelFlux.inputBeginDate('2013-10-10')
            self.ChannelFlux.searchButton()
            #统计页面数据
            totalData = [data for data in self.Table.getCellText()]
            
            #选择自有渠道
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            time.sleep(1)
            self.ChannelTree.getChannel('自有渠道')
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            #输入时间段，点击查询按钮
            self.ChannelFlux.inputBeginDate( '2013-10-10')
            self.ChannelFlux.searchButton()
            #获取自有渠道数据
            selfChannelData = [data for data in self.Table.getCellText()]
            
            #对比总渠道页面显示的自有渠道和自有渠道页面下的数据一致性
            self.assertEqual(totalData[0][1:], selfChannelData[-2][1:], 'data is not equal')
        except Exception as e:
            raise e     
        
    def estSelfChannelCompareOfflineArrivar(self):
        '''
        自有渠道比较点击线下到达的合计数据一致性
        '''
        try:
            #选择自有渠道
            self.ChannelTree.getChannel('自有渠道')
            time.sleep(1)
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            #输入时间段，点击查询
            self.ChannelFlux.inputBeginDate( '2013-10-10')
            self.ChannelFlux.searchButton()
            #获取自有渠道数据
            selfChannelData = [data for data in self.Table.getCellText()]
            
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            time.sleep(1)
            #选择线下到达模式
            self.ChannelTree.getChannelByTree('自有渠道','线下到达模式')
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            #输入时间段，点击查询
            self.ChannelFlux.inputBeginDate( '2013-10-10')
            self.ChannelFlux.searchButton()
            #获取线下到达模式数据
            offlineArrivalData = [data for data in self.Table.getCellText()]
            
            #断言。比较线下到达模式的数据
            self.assertEqual(selfChannelData[1][1:], offlineArrivalData[-2][1:], 'offlineChannelData is not equal')
        except Exception as e:
            raise e
    
    def estofflineArrivalComparescTelecom(self):
        '''
        比较四川电信的数据
        '''
        try:
            #选择线下到达模式
            self.ChannelTree.getChannelByTree('自有渠道','线下到达模式')
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            #输入时间段，点击查询
            self.ChannelFlux.inputBeginDate( '2013-10-10')
            self.ChannelFlux.searchButton()
            #获取线下到达模式数据
            offlineArrivalData = [data for data in self.Table.getCellText()]
            
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            #选择四川电信
            self.ChannelTree.getChannelByTree('线下到达模式','四川电信')
            time.sleep(1)
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            #输入时间段，点击查询
            self.ChannelFlux.inputBeginDate( '2013-10-10')
            self.ChannelFlux.searchButton()
            #获取线下到达模式数据
            scTelecomData = [data for data in self.Table.getCellText()]
            
            #断言。比较四川电信的数据
            self.assertEqual(offlineArrivalData[1][1:], scTelecomData[-2][1:], 'scTelecomData is not equal')
        except Exception as e:
            raise e
        
    def estScTelecomCompareCdTelecom(self):
        '''
        比较成都电信
        '''
        try:
            #选择四川电信
            self.ChannelTree.getChannelByTree('自有渠道','线下到达模式','四川电信')
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            #输入时间段，点击查询
            self.ChannelFlux.inputBeginDate( '2013-10-10')
            self.ChannelFlux.searchButton()
            #获取线下到达模式数据
            scTelecomData = [data for data in self.Table.getCellText()]
            
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            #选择成都电信
            self.ChannelTree.getChannelByTree('四川电信','成都电信')
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            #输入时间段，点击查询
            self.ChannelFlux.inputBeginDate( '2013-10-10')
            self.ChannelFlux.searchButton()
            #获取线下到达模式数据
            cdTelecomData = [data for data in self.Table.getCellText()]
            
            #断言。比较成都电信的数据
            self.assertEqual(scTelecomData[4][1:], cdTelecomData[-2][1:], 'cdTelecom is not equal')
        except Exception as e:
            raise e
        
    def estCdTelecomCompareJinjiang(self):
        '''
        比较锦江区数据
        '''
        try:
            #选择成都电信
            self.ChannelTree.getChannelByTree('自有渠道','线下到达模式','四川电信','成都电信')
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            #输入时间段，点击查询
            self.ChannelFlux.inputBeginDate( '2013-10-10')
            self.ChannelFlux.searchButton()
            #获取线下到达模式数据
            cdTelecomData = [data for data in self.Table.getCellText()]
            
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            #选择锦江区
            self.ChannelTree.getChannelByTree('成都电信','锦江区')
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            #输入时间段，点击查询
            self.ChannelFlux.inputBeginDate('2013-10-10')
            self.ChannelFlux.searchButton()
            #获取锦江区数据
            jinJiangData = [data for data in self.Table.getCellText()]
            
            #断言。比较锦江区数据
            self.assertEqual(cdTelecomData[5][1:], jinJiangData[-2][1:], 'jinjiangData is not equal')
        except Exception as e:
            raise e
        
    def testJinJiangCompareTaiShengRoad(self):
        '''
        比较太升南路数据
        '''
        try:
            #选择锦江区
            self.ChannelTree.getChannelByTree('自有渠道','线下到达模式','四川电信','成都电信','锦江区')
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            #输入时间段，点击查询
            self.ChannelFlux.inputBeginDate('2013-10-10')
            self.ChannelFlux.searchButton()
            #获取锦江区数据
            jinJiangData = [data for data in self.Table.getCellText()]
            
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            #选择太升南路营业厅
            self.ChannelTree.getChannelByTree('锦江区','成都太升南路65号营业厅')
            #页面跳转
            self.Menu.default_content()
            self.Menu.switchMainFrame()
            self.ChannelFlux.switchChannelFluxReort()
            time.sleep(1)
            #输入时间段，点击查询
            self.ChannelFlux.inputBeginDate('2013-10-10')
            self.ChannelFlux.searchButton()
            #获取锦江区数据
            taiShengData = [data for data in self.Table.getCellText()]
            
            #断言。比较太升南路营业厅数据
            self.assertEqual(jinJiangData[0][1:], taiShengData[-2][1:], 'taiShengData is not equal')
        except Exception as e:
            raise e
    def tearDown(self):
        self.close()
        
if __name__ == '__main__':
    unittest.main()
        