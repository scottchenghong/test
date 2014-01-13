# -*- coding:utf-8 -*-
'''
Created on 2013-11-13

@author: Cliu
'''

#import time 
from Lib.web_control import webControl

class channelLevelReport(webControl):
    '''
    商务人员提成报表
    '''
        
    def clickDetailButton(self,channelName):
        '''
        点击详细按钮
        '''
        self.click_button('//td[text()="%s"]/following-sibling::td/a[text()="[详细]"]'%(channelName))
        
    def switchChannelLevlReort(self):
        '''
        跳转到渠道流量报表页面
        '''
        self.skip_frame('authorize')
    
    def computeSum(self,channelDataAll):
        '''
        @summary: Compute each item Sum in page
        @return: 返回一个以列号为key的字典
        '''
        
        channelData = channelDataAll[0:-1]
        sumCompute = {}
        for x in range(0,len(channelData[0])):
            sumCompute[x] = 0
        
        for i in range(0,len(channelData)):
            for j in range(2,len(channelData[i])):
                if channelData[i][j].decode('utf8') != '/':
                    #print self.topChannelData[i][j]
                    sumCompute[j] += float(channelData[i][j].decode('utf8'))
        type(sumCompute)
        
        return sumCompute
    
    def compareSum(self,computedSum,pageSum):
        '''
        @summary: 比较计算出的合计与页面展示合计是否一致
        @return: 如所有值都相等，返回0，否则返回不相等信息
        '''
        msg = 0 
        for y in computedSum.keys():
            if y != 0 and y != 1:
                eachComputedSum = ('%.2f'%float(computedSum[y]))
                eachPageSum = ('%.2f'%float(pageSum[y]))
                print eachComputedSum,eachPageSum
                #print float(Sum[y]),float(self.topChannelSum[y])
                
                if eachComputedSum != eachPageSum :
                    msg = 'The %s row computed Sum is not Equal with Sum in page' %y
                    break
        return msg
    
if __name__ == '__main__':
    import time
    from selenium import webdriver
    from Page.left_menu import Left_menu
    from Page.login import Login
    from Lib.Table import Table
    from Page.report_manage.channelResourcesTree import ChannelResourcesTree
    
    driver = webdriver.Firefox()
    url = 'http://192.168.188.201/yunguan/login'
    
    UserLogin = Login(driver,url)
    Menu = Left_menu(driver,url)
    channelLeverlReport = channelLevelReport(driver,url)
    Mytable = Table(driver,url)
    Mytable = Table(driver,url)
    channelTree = ChannelResourcesTree(driver,url)
    
    try:
        UserLogin.input_usr('admin')
        UserLogin.input_pwd('cdsf_2012')
        UserLogin.click_confirm_button()
        time.sleep(1)
        
        #操作左边菜单栏，包括点击报表管理、点击渠道流量表、退出左边I1页面，进入I2页面
        Menu.switch_left_frame()
        Menu.open_report_manage()
        time.sleep(1)
        Menu.getChannelLevelReport()
        time.sleep(1)
        Menu.default_content()
        Menu.switchMainFrame()
        time.sleep(1)
        
        channelTree.openChannelTreeButton('自有渠道')
        time.sleep(1)
        channelTree.getChannel('线下到达模式')
        time.sleep(1)
        
        Menu.default_content()
        Menu.switchMainFrame()
        channelLeverlReport.switchChannelLevlReort()
        time.sleep(1)
        
        channelLeverlReport.inputBeginDate('2013-10-01')
        channelLeverlReport.inputEndDate('2013-10-10')
        channelLeverlReport.searchButton()
        time.sleep(3)
        channelLeverlReport.clickDetailButton('四川电信')
        time.sleep(3)
    except Exception as e:
        raise e
    finally:
        channelLeverlReport.close()