# coding:utf8

'''
Created on 2013-11-1

@author: chenghong
'''

from selenium import webdriver
from Lib.web_control import webControl
from Page.left_menu import Left_menu

class ListDeviceNetwork(webControl):
    '''
    联网通报报表
    '''
              
    def selectManager(self,value):
        '''
        选择渠道经理查询框进入输入
        '''
        self.input_textbox('manager', value)
        
    def selectDevice(self,value):
        '''
        输入设备号进行查询
        '''
        self.input_textbox('device', value)
        
    def selectChannel(self,value):
        '''
        输入渠道号进行查询
        '''
        self.input_textbox('channel', value)
        
    def clickSearchButton(self):
        '''
        click search button
        '''
        self.click_button("//input[@id='searchBtn']")
        
    def leadingOutReport(self):
        '''
        导出报表
        '''
        self.get_xpath('//img[@class="point"]').click()
    



if __name__ == '__main__':
    
    import time
    from Page.login import Login
    from Lib.Table import Table
    
    driver = webdriver.Firefox()
    url = 'http://192.168.188.201/yunguan/login'
    
    User_login = Login(driver,url)
    Menu = Left_menu(driver,url)
    User_search_report = ListDeviceNetwork(driver,url)
    Mytable = Table(driver,url)
    Mytable = Table(driver,url)
    
    try:
        User_login.input_usr('admin')
        User_login.input_pwd('cdsf_2012')
        User_login.click_confirm_button()
        
        Menu.switch_left_frame()
        Menu.open_report_manage()
        
        time.sleep(3)
        
        Menu.clickListDeviceNetwork()
        Menu.default_content()
        Menu.switchMainFrame()
        
        time.sleep(4)
        
#         User_search_report.selectManager(u'测试')
#         User_search_report.leadingOutReport()
#         User_search_report.clickSearchButton()
        time.sleep(3)
        User_search_report.getDatePicker('time','2013-11-1 17:30:00')
        User_search_report.clickSearchButton()
        time.sleep(5)
        MyTableClass = '//table[@class="table_data"]//tr'
        tablelist = Mytable.getCellText(MyTableClass)
        print tablelist[0][0],tablelist[0][1]
    except Exception as e:
        print e
    finally:
        User_login.close()
        
        