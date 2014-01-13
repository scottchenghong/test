# -*- coding:utf-8 -*-
'''
Created on Jul 9, 2013

@author: chenghong
'''
import time
import selenium.webdriver as webdriver
from Lib.web_control import webControl 
from Page.login import Login

class TopFrame(webControl):
    '''
    该类主要针对登陆后主页面的顶部页面的3个功能进行独立封装，具体如下：
    1、包括“欢迎登陆”显示当前登陆账号；
    2、密码修改；
    3、退出登陆。
    '''
    
    def switchTopFrame(self):
        '''
        跳转页面至top
        '''
        self.skip_frame('topFrame')
        
    def getWelcomeLogin(self):
        '''
        welcome to login
        '''
        return self.get_xpath("//div[@class='top_admin']/p/span").text
    
    def changeGwd(self):
        '''
        修改密码
        '''
        self.click_button("//img[@src='/yunguan/static/images/top_photo2.jpg']")
        
    def loginOut(self):
        '''
        退出登陆
        '''
        self.click_button("//img[@src='/yunguan/static/images/top_photo3.jpg']")
        
        
if __name__ == '__main__':
    #赋值参数
    url = 'http://192.168.188.201/yunguan/login'
    driver = webdriver.Firefox()
    
    #实例化对象
    User_login = Login(driver,url)
    top_frame = TopFrame(driver,url)
    try:
        
        #用户登陆
        User_login.input_usr('admin')
        User_login.input_pwd('cdsf_2012')
        User_login.click_confirm_button()
        
        top_frame.switchTopFrame()
        
        print top_frame.getWelcomeLogin()
#         top_frame.changeGwd()
#         time.sleep(3)
        top_frame.loginOut()
        print '退出登陆'
        time.sleep(3)
        User_login.input_usr('liuxinrui')
        User_login.input_pwd('cdsf_2012')
        User_login.click_confirm_button()
    except Exception as e:
        print e
    finally:
        top_frame.close()