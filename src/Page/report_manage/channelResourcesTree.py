#coding:utf8

'''
Created on 2013-11-8

@author: chenghong
'''
import time
from selenium import webdriver
from Lib.web_control import webControl

class ChannelResourcesTree(webControl):
    '''
    渠道树
    '''    
        
    def getChannel(self,channelName):
        '''
        @param channelName: 要点击的渠道名称 
        '''
        print channelName
        self.get_xpath('//a[@title="%s"]' %(channelName)).click()
        
    def openChannelTreeButton(self,channelName):
        '''
        点击对应渠道的展开按钮
        '''
        #通过渠道名称查找它的前一兄弟节点即展开按钮标签
        self.get_xpath('//a[@title="%s"]/preceding-sibling::*' %(channelName)).click()
    def getChannelByTree(self,*args): 
        #如渠道层级大于1，则依次展开直到需要倒数第二级渠道

        if len(args) > 1:
            for arg in args[0:-1]:
                self.openChannelTreeButton(arg)
                time.sleep(1)
            self.getChannel(args[-1])
        #如渠道等于1，则直接点击需要查看的渠道
        elif len(args) == 1:
            self.getChannel(args)
            
        
if __name__ == '__main__':
    
    from Page.login import Login
    from Page.left_menu import Left_menu
    
    driver = webdriver.Firefox()
    url = 'http://192.168.188.201/yunguan/login'
    
    User_login = Login(driver,url)
    Menu = Left_menu(driver,url)
    channeltree = ChannelResourcesTree(driver,url)
    
    try:
        User_login.input_usr('admin')
        User_login.input_pwd('cdsf_2012')
        User_login.click_confirm_button()
        time.sleep(1)
        
        Menu.switch_left_frame()
        Menu.open_report_manage()
        time.sleep(1)
        Menu.getChannelFluxReport()
        time.sleep(3)
        
        Menu.default_content()
        Menu.switchMainFrame()
        time.sleep(1)
        
        channeltree.getChannelByTree('自有渠道','线下到达模式','四川电信')
        time.sleep(5)
    except Exception as e:
        print e
    finally:
        channeltree.close()