#coding:utf8

'''
Created on 2013-11-8

@author: chenghong
'''
import time
from selenium import webdriver
from Lib.web_control import webControl
from Page.left_menu import Left_menu
from Page.login import Login
from Lib.Table import Table
from Page.report_manage.channelResourcesTree import ChannelResourcesTree

class channelFluxReport(webControl):
    '''
    渠道流量报表
    '''
    def searchButton(self):
        self.click_button("//input[@id='searchBtn']")
        
    def switchChannelFluxReort(self):
        '''
        跳转到渠道流量报表页面
        '''
        self.skip_frame('authorize')
        

if __name__ == '__main__':
    
    driver = webdriver.Firefox()
    url = 'http://192.168.188.201/yunguan/login'
    
    UserLogin = Login(driver,url)
    Menu = Left_menu(driver,url)
    channelFluxReport = channelFluxReport(driver,url)
    Mytable = Table(driver,url)
    Mytable = Table(driver,url)
    channelTree = ChannelResourcesTree(driver,url) 
    
    try:
        UserLogin.input_usr('admin')
        UserLogin.input_pwd('cdsf_2012')
        UserLogin.click_confirm_button()
        time.sleep(3)
        
        #操作左边菜单栏，包括点击报表管理、点击渠道流量表、退出左边I1页面，进入I2页面
        Menu.switch_left_frame()
        Menu.open_report_manage()
        time.sleep(2)
        Menu.getChannelFluxReport()
        time.sleep(3)
        Menu.default_content()
        Menu.switchMainFrame()
        time.sleep(3)
        
        channelTree.openChannelTreeButton('自有渠道')
        time.sleep(1)
        channelTree.getChannel('线下到达模式')
        time.sleep(3)
        
        Menu.default_content()
        Menu.switchMainFrame()
        channelFluxReport.switchChannelFluxReort()
        time.sleep(3)
        
        channelFluxReport.getDatePicker('beginDate','2013-10-10')
        time.sleep(2)
        channelFluxReport.searchButton()
        time.sleep(3)
    except Exception as e:
        print e
    finally:
        Menu.close()
        
        