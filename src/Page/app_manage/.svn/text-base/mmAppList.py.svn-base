#coding:utf8

'''
Created on 2013-11-20

@author: chenghong
'''
import time
from Lib.web_control import webControl


class MMAppList(webControl):
    '''
    移动MM市场获取APP信息并生成下载地址，实现后台进行下载APP功能
    '''
    
    def clickMMAppList(self):
        '''
        点击'移动渠道应用获取'
        '''
        self.click_button('//a[@id="mmappList"]')
        
    def inputAppName(self,value):
        '''
        输入应用名称进行查询
        '''
        self.input_textbox('name', value)
        
    def clickSearchButton(self):
        '''
        点击查询按钮
        '''
        self.click_button('//img[@id="_appSearch"]')
        
    def clickDownLoadApp(self,appName):
        '''
        点击下载按钮
        @param appName: 要下载的appName 
        '''
        self.click_button('//td[text()="%s"]/following-sibling::td/div/a[text()="下载"]' %(appName))
        
        
if __name__ == '__main__':
    
    from selenium import webdriver
    from Page.login import Login
    from Page.left_menu import Left_menu
    from Lib.Table import Table
    
    driver = webdriver.Firefox()
    url = "http://192.168.188.201/yunguan/login"
    
    login = Login(driver,url)
    menu = Left_menu(driver,url)
    mm = MMAppList(driver,url)
    table = Table(driver,url)
    
    
    try:
        login.input_usr('admin')
        login.input_pwd('cdsf_2012')
        login.click_confirm_button()
        time.sleep(2)
        #跳转到左边菜单，点击应用管理
        menu.switch_left_frame()
        menu.click_app_manege()
        time.sleep(3)
        #点击"移动渠道应用获取"
        mm.clickMMAppList()
        
        #跳出原来页面，进入新页面
        menu.default_content()
        menu.switchMainFrame()
        print 'switch successful'
        time.sleep(2)
        
        #输入应用名称，点击查询按钮
        mm.inputAppName(u'金手指')
        mm.clickSearchButton()
        time.sleep(3)
        
        #获取页面form数据
        for data in table.getCellText():
            for i in data:
                print i
                
        #选择应用进行下载操作
        mm.clickDownLoadApp('金手指')
        print 'download successful!'
    except Exception as e:
        print e
    finally:
        driver.close()