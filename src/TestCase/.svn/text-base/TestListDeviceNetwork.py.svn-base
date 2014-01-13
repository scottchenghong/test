# -*- coding:utf-8 -*-

'''
Created on 2013-11-5

@author: chenghong
'''

import time
import unittest
from selenium import webdriver
import TestPremiseCaseLogin as login
from Page.left_menu import Left_menu
from Page.report_manage.listDeviceNetwork import ListDeviceNetwork
from Lib.WebBase import WebBase
from Lib.Mysql import Mysql
from Lib.Table import Table
from Lib.Util import PageSqlCompare

class TestListDeviceNetwork(unittest.TestCase,WebBase):
    '''
    测试联网通报报表的业务功能。包括条件查询、页面查询结果对比
    '''
    def setUp(self):
        '''
        '''
        self.user = 'admin'
        self.pwd= 'cdsf_2012'
        self.url = 'http://192.168.188.201/yunguan/login'
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        
        self.Menu = Left_menu(self.driver,self.url)
        self.Report = ListDeviceNetwork(self.driver,self.url)
        self.Mysql = Mysql()
        self.Table = Table(self.driver,self.url)
        self.dateTime = '2013-11-11 17:30:00'
        self.deviceCode = u'SF0009'
        self.channelName = u'成都市'
        self.realName = u'测试'
        
        
        self.DeviceSql ="""
        SELECT D2.REALNAME,D2.NAME,D2.DEVICE,D2.CREATE_TIME, D2.LAST_TIME FROM \
        ( SELECT get_channel_manager_realname(C.CHANNEL_ID) AS REALNAME , IF(C.DEVICE_ALIAS \
        IS NULL OR TRIM(C.DEVICE_ALIAS)='',C.DEVICE_CODE,TRIM(C.DEVICE_ALIAS)) as DEVICE,\
         G. NAME, DATE_FORMAT(C.CREATE_TIME,"%%Y-%%m-%%d %%H:%%i:%%s" )AS CREATE_TIME ,\
         IFNULL(DATE_FORMAT(D1.LAST_TIME,"%%Y-%%m-%%d %%H:%%i:%%s" ), '-')AS LAST_TIME \
         FROM CK_DEVICE C LEFT JOIN( SELECT CDS.DEVICE_CODE, MAX(CDS.CREATE_TIME)AS \
         LAST_TIME FROM CK_DEVICE_STATUS CDS WHERE CDS.CREATE_TIME <= \
         STR_TO_DATE(%s, "%%Y-%%m-%%d %%H:%%i:%%s") GROUP BY CDS.DEVICE_CODE )D1\
         ON D1.DEVICE_CODE = C.DEVICE_CODE LEFT JOIN YG_CHANNEL_GD G ON G.ID = \
         C.CHANNEL_ID WHERE C.STATE = 1 AND C.CREATE_TIME <= STR_TO_DATE(%s, \
         "%%Y-%%m-%%d %%H:%%i:%%s") ) D2 WHERE 1=1 AND UPPER(D2.DEVICE) \
         LIKE CONCAT('%%',%s,'%%') ORDER BY REALNAME DESC, NAME DESC limit 0 ,10
        """
        
        self.realNameSql="""
        SELECT D2.REALNAME, D2.NAME, D2.DEVICE, D2.CREATE_TIME, D2.LAST_TIME FROM \
        ( SELECT get_channel_manager_realname(C.CHANNEL_ID) AS REALNAME , \
        IF(C.DEVICE_ALIAS IS NULL OR TRIM(C.DEVICE_ALIAS)='',C.DEVICE_CODE,\
        TRIM(C.DEVICE_ALIAS)) as DEVICE, G. NAME, DATE_FORMAT(C.CREATE_TIME,\
        "%%Y-%%m-%%d %%H:%%i:%%s" )AS CREATE_TIME ,IFNULL(DATE_FORMAT(D1.LAST_TIME,\
        "%%Y-%%m-%%d %%H:%%i:%%s" ), '-')AS LAST_TIME FROM CK_DEVICE C LEFT \
        JOIN( SELECT CDS.DEVICE_CODE, MAX(CDS.CREATE_TIME)AS LAST_TIME FROM \
        CK_DEVICE_STATUS CDS WHERE CDS.CREATE_TIME <= STR_TO_DATE(%s, "%%Y-%%m-%%d \
        %%H:%%i:%%s") GROUP BY CDS.DEVICE_CODE )D1 ON D1.DEVICE_CODE = C.DEVICE_CODE \
        LEFT JOIN YG_CHANNEL_GD G ON G.ID = C.CHANNEL_ID WHERE C.STATE = 1 AND \
        C.CREATE_TIME <= STR_TO_DATE(%s, "%%Y-%%m-%%d %%H:%%i:%%s") ) D2 WHERE 1=1 \
        AND LOWER(D2.REALNAME) LIKE CONCAT('%%',%s,'%%') ORDER BY REALNAME DESC, \
        NAME DESC limit 0 ,10
        """
        
        self.channelNameSql = """
        SELECT D2.REALNAME, D2.NAME,D2.DEVICE, D2.CREATE_TIME, D2.LAST_TIME \
        FROM ( SELECT get_channel_manager_realname(C.CHANNEL_ID) AS REALNAME , \
        IF(C.DEVICE_ALIAS IS NULL OR TRIM(C.DEVICE_ALIAS)='',C.DEVICE_CODE,\
        TRIM(C.DEVICE_ALIAS)) as DEVICE, G. NAME, DATE_FORMAT(C.CREATE_TIME,\
        "%%Y-%%m-%%d %%H:%%i:%%s" )AS CREATE_TIME ,IFNULL(DATE_FORMAT\
        (D1.LAST_TIME,"%%Y-%%m-%%d %%H:%%i:%%s" ), '-')AS LAST_TIME FROM \
        CK_DEVICE C LEFT JOIN( SELECT CDS.DEVICE_CODE, MAX(CDS.CREATE_TIME)AS \
        LAST_TIME FROM CK_DEVICE_STATUS CDS WHERE CDS.CREATE_TIME <= \
        STR_TO_DATE(%s, "%%Y-%%m-%%d %%H:%%i:%%s") GROUP BY CDS.DEVICE_CODE )D1 \
        ON D1.DEVICE_CODE = C.DEVICE_CODE LEFT JOIN YG_CHANNEL_GD G ON G.ID = \
        C.CHANNEL_ID WHERE C.STATE = 1 AND C.CREATE_TIME <= STR_TO_DATE(%s, \
        "%%Y-%%m-%%d %%H:%%i:%%s") ) D2 WHERE 1=1 AND LOWER(D2.NAME) LIKE \
        CONCAT('%%',%s,'%%') ORDER BY REALNAME DESC, NAME DESC limit 0 ,10
        """
        
        self.onlyDateTimeSql = """
        SELECT D2.REALNAME, D2.NAME,D2.DEVICE,D2.CREATE_TIME, D2.LAST_TIME FROM \
        ( SELECT get_channel_manager_realname(C.CHANNEL_ID) AS REALNAME , \
        IF(C.DEVICE_ALIAS IS NULL OR TRIM(C.DEVICE_ALIAS)='',C.DEVICE_CODE,\
        TRIM(C.DEVICE_ALIAS)) as DEVICE, G. NAME, DATE_FORMAT(C.CREATE_TIME,\
        "%%Y-%%m-%%d %%H:%%i:%%s" )AS CREATE_TIME ,IFNULL(DATE_FORMAT(D1.LAST_TIME,\
        "%%Y-%%m-%%d %%H:%%i:%%s" ), '-')AS LAST_TIME FROM CK_DEVICE C LEFT JOIN( \
        SELECT CDS.DEVICE_CODE, MAX(CDS.CREATE_TIME)AS LAST_TIME FROM CK_DEVICE_STATUS \
        CDS WHERE CDS.CREATE_TIME <= STR_TO_DATE(%s, "%%Y-%%m-%%d %%H:%%i:%%s") \
        GROUP BY CDS.DEVICE_CODE )D1 ON D1.DEVICE_CODE = C.DEVICE_CODE LEFT JOIN \
        YG_CHANNEL_GD G ON G.ID = C.CHANNEL_ID WHERE C.STATE = 1 AND C.CREATE_TIME \
        <= STR_TO_DATE(%s, "%%Y-%%m-%%d %%H:%%i:%%s") ) D2 WHERE 1=1 ORDER BY REALNAME \
        DESC, NAME DESC limit 0 ,10 
        """
        
        self.deviceChannelRealNameSql = """
        SELECT D2.REALNAME, D2.NAME, D2.DEVICE, D2.CREATE_TIME, D2.LAST_TIME FROM \
        ( SELECT get_channel_manager_realname(C.CHANNEL_ID) AS REALNAME , \
        IF(C.DEVICE_ALIAS IS NULL OR TRIM(C.DEVICE_ALIAS)='',C.DEVICE_CODE,\
        TRIM(C.DEVICE_ALIAS)) as DEVICE, G. NAME, DATE_FORMAT(C.CREATE_TIME,\
        "%%Y-%%m-%%d %%H:%%i:%%s" )AS CREATE_TIME ,IFNULL(DATE_FORMAT(D1.LAST_TIME,\
        "%%Y-%%m-%%d %%H:%%i:%%s" ), '-')AS LAST_TIME FROM CK_DEVICE C LEFT \
        JOIN( SELECT CDS.DEVICE_CODE, MAX(CDS.CREATE_TIME)AS LAST_TIME FROM \
        CK_DEVICE_STATUS CDS WHERE CDS.CREATE_TIME <= STR_TO_DATE(%s, \
        "%%Y-%%m-%%d %%H:%%i:%%s") GROUP BY CDS.DEVICE_CODE )D1 ON D1.DEVICE_CODE \
        = C.DEVICE_CODE LEFT JOIN YG_CHANNEL_GD G ON G.ID = C.CHANNEL_ID WHERE \
        C.STATE = 1 AND C.CREATE_TIME <= STR_TO_DATE(%s, "%%Y-%%m-%%d %%H:%%i:%%s") \
        ) D2 WHERE 1=1 AND UPPER(D2.DEVICE) LIKE CONCAT('%%',%s,'%%') AND \
        LOWER(D2.NAME) LIKE CONCAT('%%',%s,'%%') AND LOWER(D2.REALNAME) \
        LIKE CONCAT('%%',%s,'%%') ORDER BY REALNAME DESC, NAME DESC limit 0 ,10
        """
        
        try:
            #admin用户登陆后台
            login.getUserLogin(self.driver, self.url, self.user, self.pwd)
            
            time.sleep(2)
             
            #页面跳转至左边菜单并分别依次点击'报表管理'、'联网通报报表'
            self.Menu.switch_left_frame()
            self.Menu.open_report_manage()
             
            time.sleep(2)
             
            self.Menu.clickListDeviceNetwork()
             
            time.sleep(3)
             
            #跳出左边frame
            self.Menu.default_content()
            time.sleep(3)
            #页面跳转至报表主页面
            self.Menu.switchMainFrame()
            print '跳转页面成功'
        except Exception as e:
            print e
        
    def testSearchData(self):
        '''
                测试按时间查询报表是否成功
        '''
        try:
            #搜索条件选择日期进行查询
            self.Report.getDatePicker('time',self.dateTime)
            #点击查询按钮
            self.Report.clickSearchButton()
            #获取页面数据
            pageSecletDataAll = self.Table.getCellText('//table[@class="table_data"]//tr')
            pageSecletData = pageSecletDataAll[0:-1]
            #查询数据库中数据 
            sqlData = self.Mysql.selectAllData(self.onlyDateTimeSql,self.dateTime,self.dateTime)
            #判断页面数据是否与数据库中数据一致
            Equal = PageSqlCompare(pageSecletData,sqlData)
            #断言。判断该业务是否执行成功
            self.assertEqual(Equal, 1, u'数据库中数据于页面数据不一致')
        except Exception as e:
            return e
         
    def testSearchManager(self):
        '''
                测试按渠道经理进行查询是否成功
        '''
         
        try:
           
            #搜索条件选择渠道经理选项，且文本框输入'测试'
            self.Report.selectManager(self.realName)
            #点击查询按钮
            self.Report.clickSearchButton()
            
            
            #获取页面数据
            pageSecletDataAll = self.Table.getCellText('//table[@class="table_data"]//tr')
            pageSecletData = pageSecletDataAll[0:-1]
            #查询数据库中数据 
            sqlData = self.Mysql.selectAllData(self.realNameSql,self.dateTime,self.dateTime,self.realName.encode("utf8"))
            #判断页面数据是否与数据库中数据一致
            Equal = PageSqlCompare(pageSecletData,sqlData)
            #断言。判断该业务是否执行成功
            self.assertEqual(Equal, 1, u'数据库中数据于页面数据不一致')
             
        except Exception as e:
            return e
         
    def testSearchDevice(self):
        '''
                按设备号进行查询
        '''
         
        try:
            #搜索条件选择设备号选项，且文本框输入'测试'
            self.Report.selectDevice(self.deviceCode)
            #点击查询按钮
            self.Report.clickSearchButton()
            
            #获取页面数据
            pageSecletDataAll = self.Table.getCellText('//table[@class="table_data"]//tr')
            pageSecletData = pageSecletDataAll[0:-1]
            #查询数据库中数据 
            sqlData = self.Mysql.selectAllData(self.DeviceSql,self.dateTime,self.dateTime,self.deviceCode.encode("utf8"))
            #判断页面数据是否与数据库中数据一致
            Equal = PageSqlCompare(pageSecletData,sqlData)
            #断言。判断该业务是否执行成功
            self.assertEqual(Equal, 1, u'数据库中数据于页面数据不一致')
            
        except Exception as e:
            return e
         
    def testSearchChannel(self):
        '''
                按渠道名称进行查询
        '''
         
        try:
            #搜索条件选择渠道名称选项，且文本框输入'测试'
            self.Report.selectChannel(self.channelName)
            #点击查询按钮
            self.Report.clickSearchButton()
            
            #获取页面数据
            pageSecletDataAll = self.Table.getCellText('//table[@class="table_data"]//tr')
            pageSecletData = pageSecletDataAll[0:-1]
            #查询数据库中数据 
            sqlData = self.Mysql.selectAllData(self.channelNameSql,self.dateTime,self.dateTime,self.channelName.encode("utf8"))
            #判断页面数据是否与数据库中数据一致
            Equal = PageSqlCompare(pageSecletData,sqlData)
            #断言。判断该业务是否执行成功
            self.assertEqual(Equal, 1, u'数据库中数据于页面数据不一致')
             
        except Exception as e:
            return e
         
    def testSearchManagerDeviceChannel(self):
        '''
                按渠道经理、设备号、渠道号同时进行查询
        '''
         
        try:
            #搜索条件选择渠道经理选项，且文本框输入'测试'
            self.Report.selectManager(self.realName)
            time.sleep(2)
            #搜索条件选择设备号选项，且文本框输入'测试'
            self.Report.selectDevice(self.deviceCode)
            time.sleep(3)
            #搜索条件选择渠道名称选项，且文本框输入'测试'
            self.Report.selectChannel(self.channelName)
            time.sleep(3)
            #点击查询按钮
            self.Report.clickSearchButton()
           
            #获取页面数据
            pageSecletDataAll = self.Table.getCellText('//table[@class="table_data"]//tr')
            pageSecletData = pageSecletDataAll[0:-1]
            #查询数据库中数据 
            sqlData = self.Mysql.selectAllData(self.deviceChannelRealNameSql,self.dateTime,self.dateTime,\
                                               self.deviceCode.encode("utf8"),self.channelName.encode("utf8"),self.realName.encode("utf8"))
            #判断页面数据是否与数据库中数据一致
            Equal = PageSqlCompare(pageSecletData,sqlData)
            #断言。判断该业务是否执行成功
            self.assertEqual(Equal, 1, u'数据库中数据于页面数据不一致')
            
        except Exception as e:
            return e
             
    def tearDown(self):
        self.close()
        
        
if __name__ == '__main__':
    unittest.main()