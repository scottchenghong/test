# -*- coding:utf-8 -*-
'''
Created on Jun 26, 2013

@author: chenghong
'''

from selenium import webdriver

class WebBase:
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
        self.driver.get(url)
    
    def close(self):
        self.driver.close()

if __name__ == '__main__' :
    
    dr = webdriver.Firefox( )
    url = 'http://baidu.com/'
    
    try:
        webbase = WebBase(dr,url)
        webbase.close()
    except Exception as e:
        raise e
        
