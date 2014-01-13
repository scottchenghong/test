# coding:utf8

'''
Created on 2013-11-13
@author: chenghong
'''

import time
from selenium import webdriver
from Lib.web_control import webControl
from Page.login import Login
from Page.left_menu import Left_menu
from Lib.Table import Table

class InteriorPushMoneyTotalReport(webControl):
    '''
    商务人员提成报表
    '''
    
    def inputUserName(self,value):
        '''
        人员输入框
        '''
        self.input_textbox('userName', value)
        
    def clickDetailButton(self,userName):
        '''
        点击详细按钮
        '''
        self.click_button('//td[text()="%s"]/following-sibling::td/a[text()="[详细]"]'%(userName))
    
    
        
if __name__ == '__main__':
    
    from Lib import pagewait   
    driver = webdriver.Firefox()
    url = 'http://192.168.188.201/yunguan/login'
    
    login = Login(driver,url)
    menu = Left_menu(driver,url)
    table = Table(driver,url)
    interior = InteriorPushMoneyTotalReport(driver,url)
    
    try:
        #用户登陆
        login.input_usr('admin')
        login.input_pwd('cdsf_2012')
        login.click_confirm_button()
        
        #等待页面加载
        pagewait.waitPage(driver,'//frame[@id="mainFrame"]', 'login failed')
        
        #操作左边菜单
        menu.switch_left_frame()
        menu.open_report_manage()
        time.sleep(2)
        pagewait.waitPage(driver,'//a[text()="商务人员提成报表"]', 'open reportManage failed')
        menu.getInteriorPushMoneyTotalReport()
        
        menu.default_content()
        menu.switchMainFrame()
        
        #输入人员名称、时间,点击查询查询
#         interior.inputUserName(u'丁迪')
        interior.inputBeginDate('2013-11-01')
        interior.inputEndDate('2013-11-10')
        interior.searchButton()
        pagedata = table.getCellText()[:-1]
        
        for data in pagedata:
            print data[-1]
        time.sleep(5)
        interior.clickDetailButton('丁迪')
        print '=========================='
        print '跳转成功'
        print '=========================='
        
        data = table.getCellText('//table[@class="table_data"]//tr')[:-1]
        sum = 0
        for cell in data:
            sum += float(cell[-1])
        print sum
    except Exception as e:
        raise e
    finally:
        menu.close()
    
    