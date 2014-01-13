#coding:utf8

'''
Created on 2013-11-18

@author: chenghong
'''

from selenium.webdriver.support.ui import WebDriverWait

def waitPage(driver,xpath,msg):
    '''
    等待页面加载完毕
    @param driver:浏览器驱动 
    @param xpath:需要查找的页面元素xpath路径
    @param msg:加载失败信息  
    '''

    #实例化wait对象
    webWait = WebDriverWait(driver,10)
    
    webWait.until(lambda driver:driver.find_elements_by_xpath(xpath), msg)