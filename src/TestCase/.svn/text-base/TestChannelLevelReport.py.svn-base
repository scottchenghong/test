# -*- coding:utf-8 -*-
'''
Created on 2013-11-13

@author: Cliu
'''

import time
import unittest
from selenium import webdriver
import TestPremiseCaseLogin as login
from Page.left_menu import Left_menu
from Page.report_manage.channelLevelReport import channelLevelReport
from Page.report_manage.channelResourcesTree import ChannelResourcesTree 
from Lib.WebBase import WebBase
from Lib.Mysql import Mysql
from Lib.Table import Table
#from Lib.Util import PageSqlCompare

class TestChannelLevelReport(unittest.TestCase,WebBase):
    """
    """
    
    def setUp(self):
        """
                初始化页面至渠道报表页面
        """
        self.user = 'admin'
        self.pwd= 'cdsf_2012'
        self.url = 'http://192.168.188.201/yunguan/login'
        self.startTime = '2012-10-10'
        self.endTime = '2013-10-10'
        self.driver = webdriver.Firefox()
        #self.driver.implicitly_wait(10)
        
        self.Menu = Left_menu(self.driver,self.url)
        self.Report = channelLevelReport(self.driver,self.url)
        self.channelTree = ChannelResourcesTree(self.driver,self.url)
        
        self.Mysql = Mysql()
        self.Table = Table(self.driver,self.url)
        
        try:
            #用户登陆
            login.getUserLogin(self.driver,self.url,self.user,self.pwd)
             
            time.sleep(3)
             
            #页面跳转至左边菜单并分别依次点击'报表管理'、'渠道报表'
            self.Menu.switch_left_frame()
            self.Menu.open_report_manage()
            time.sleep(3)
            self.Menu.get_channel_level_report()
            time.sleep(3)
            self.Menu.default_content()
            time.sleep(3)
            #页面跳转至报表主页面
            self.Menu.switchMainFrame()
            time.sleep(3)
        except Exception as e:
            return e
        
        
    def estpChannelSum(self):
            
        #点击总渠道
        self.channelTree.getChannel('总渠道')
        
        #页面跳转
        self.Menu.default_content()
        self.Menu.switchMainFrame()
        self.Report.switchChannelLevlReort()
        
        #输入开始结束时间
        self.Report.inputBeginDate(self.startTime)
        self.Report.inputEndDate(self.endTime)
        time.sleep(2)
        
            
        self.Report.searchButton()
        time.sleep(1)
        #获得总渠道表页面表格内数据
        self.topChannelDataAll = self.Table.getCellText()
        #页面展示合计数据
        self.topChannelSumPage = self.topChannelDataAll[-1]
        #计算出的合计数据
        self.topComputedSum = self.Report.computeSum(self.topChannelDataAll)
        Equal = self.Report.compareSum(self.topComputedSum,self.topChannelSumPage)
        
        #断言，判断页面数据比对结果是否一致，不一致返回错误信息            
        self.assertEqual(Equal, 0,Equal)
    
    
    def ChannelSum(self,channelName):
        '''
        @summary:点击渠道查看渠道数据比较合计是否相等
        @return: 返回比较结果值
        
        '''
        #点击渠道
        self.channelTree.getChannel(channelName)
       
        #页面跳转
        self.Menu.default_content()
        self.Menu.switchMainFrame()
        self.Report.switchChannelLevlReort()
        
        #输入开始结束时间
        self.Report.inputBeginDate(self.startTime)
        self.Report.inputEndDate(self.endTime)
        time.sleep(2)
        
        self.Report.searchButton()
        time.sleep(1)
        #获总渠道表页面表格内数据
        self.topChannelDataAll = self.Table.getCellText()
        #页面展示合计数据
        self.topChannelSumPage = self.topChannelDataAll[-1]
        #计算出的合计数据
        self.topComputedSum = self.Report.computeSum(self.topChannelDataAll)
        Equal = self.Report.compareSum(self.topComputedSum,self.topChannelSumPage)     
        return Equal
    
    def channelSum(self,*args):
        '''
        @param param: *args可变参数，表示需要查看的层级，从初始层级到需要查看的层级的一个列表
        @summary: 根据渠道层级依次展开到需要查看的层级并点击需要查看的渠道并查询数据并比较sum值是否正确
        @return: 返回比较结果值
        '''
        #如渠道层级大于1，则依次展开直到需要倒数第二级渠道
        if len(args) > 1:
            for arg in args[0:-1]:
                self.channelTree.openChannelTreeButton(arg)
                time.sleep(1)
            self.channelTree.getChannel(args[-1])
        #如渠道等于1，则直接点击需要查看的渠道
        elif len(args) == 1:
            self.channelTree.getChannel(args)
            
        #页面跳转
        self.Menu.default_content()
        self.Menu.switchMainFrame()
        self.Report.switchChannelLevlReort()
        
        #输入开始结束时间
        self.Report.inputBeginDate(self.startTime)
        self.Report.inputEndDate(self.endTime)
        time.sleep(2)
        
        self.Report.searchButton()
        time.sleep(3)
        #获总渠道表页面表格内数据
        self.channelDataAll = self.Table.getCellText()
        time.sleep(2)
        #页面展示合计数据
        self.topChannelSumPage = self.channelDataAll[-1]
        #计算出的合计数据
        self.topComputedSum = self.Report.computeSum(self.channelDataAll)
        Equal = self.Report.compareSum(self.topComputedSum,self.topChannelSumPage)     
        return Equal
    
    def ChannelDetailCompare(self,channelName,*args):
        
        '''
        @param detailChannel:指需要查询详细的渠道名称 
        @param *argv: 指需要需要看详细渠道的层级
        @return: 返回比较结果
        '''
        if len(args) > 1:
            for arg in args[0:-1]:
                self.channelTree.openChannelTreeButton(arg)
                time.sleep(1)
            self.channelTree.getChannel(args[-1])
        #如渠道等于1，则直接点击需要查看的渠道
        elif len(args) == 1:
            self.channelTree.getChannel(args[0])
        
        #页面跳转
        time.sleep(1)
        self.Menu.default_content()
        self.Menu.switchMainFrame()
        self.Report.switchChannelLevlReort()
        
        #输入开始结束时间
        self.Report.inputBeginDate(self.startTime)
        self.Report.inputEndDate(self.endTime)
        print 'test3'
        self.Report.searchButton()
        time.sleep(3)
#         #获总渠道表页面表格内数据
#         print 'test0'
#         self.channelData = self.Table.getCellText()[:-1]
#         print self.channelData[0]
#         print 'test01'
        
        self.Report.clickDetailButton(channelName)
        time.sleep(2)
        self.channelDataDetail = self.Table.getOneCellText('合计')
        Equal =0
        if self.channelData[2] != self.channelDataDetail[2]:
            Equal = '渠道安装量与详细中安装量不一致'
        
        return Equal
        
    
    def estSelfChannelSum(self):
        '''
        @summary:判断自有渠道相加Sum值与页面合计值一致
        '''
        selfChannelSumIsTrue = self.ChannelSum('自有渠道')
        #断言，判断自有渠道相加Sum值与页面合计值一致
        self.assertEqual(selfChannelSumIsTrue, 0,selfChannelSumIsTrue)
    
    def estWMChannelSum(self):
        '''
        @summary:判断网盟渠道相加Sum值与页面合计值一致
        '''
        wmchannelSumIsTrue = self.ChannelSum('网盟渠道')
        #断言，判断自有渠道相加Sum值与页面合计值一致
        self.assertEqual(wmchannelSumIsTrue, 0,wmchannelSumIsTrue)      
        
    def estOPChannelSum(self):
        '''
        @summary:判断运营商渠道相加Sum值与页面合计值一致
        '''
        OPchannelSumIsTrue = self.ChannelSum('运营商渠道')
        #断言，判断自有渠道相加Sum值与页面合计值一致
        self.assertEqual(OPchannelSumIsTrue, 0,OPchannelSumIsTrue)              
    
    def estOffLineArrive(self):
        '''
        @summary: 判断线下到达模式Sum值与页面合计值一致
        '''
        OffLineArriveSum = self.channelSum('自有渠道','线下到达模式')
        #断言，判断自有渠道相加Sum值与页面合计值一致
        self.assertEqual(OffLineArriveSum, 0,OffLineArriveSum)     
    
    def estOffLineAcitive(self):
        '''
        @summary: 判断线下激活模式Sum值与页面合计值一致
        '''
        OffLineActiveSum = self.channelSum('自有渠道','线下激活模式')
        #断言，判断自有渠道相加Sum值与页面合计值一致
        self.assertEqual(OffLineActiveSum, 0,OffLineActiveSum)   
    
    def estScChinaNetChannel(self):
        #ScChinaNetSum = self.channelTree.getChannelByTree('自有渠道','线下到达模式','四川电信')
        ScChinaNetSum = self.channelSum('自有渠道','线下到达模式','四川电信')
        self.assertEqual(ScChinaNetSum, 0,ScChinaNetSum)
    
    def estCdChinaNetChannel(self):
        CdChinaNetSum = self.channelSum('自有渠道','线下到达模式','四川电信','成都电信')
        self.assertEqual(CdChinaNetSum, 0,CdChinaNetSum)
        
    def estJinNiuChinaNetChannel(self):
        JinNiuChinaNetSum = self.channelSum('自有渠道','线下到达模式','四川电信','成都电信','金牛区')
        self.assertEqual(JinNiuChinaNetSum, 0,JinNiuChinaNetSum)
        
    def estTingDianChinaNetChannel(self):
        TingDian = self.channelSum('自有渠道','线下到达模式','四川电信','成都电信','金牛区','成都一环路北四段104号天翼专营店厅')
        self.assertEqual(TingDian, 0,TingDian)
    
    def testChannelDetail(self):
        testEqual = self.ChannelDetailCompare('四川电信','自有渠道','线下到达模式')
        self.assertEqual(testEqual, 0, testEqual)
    
    def tearDown(self):
        self.close()
        
if __name__ == '__main__':
    unittest.main()
