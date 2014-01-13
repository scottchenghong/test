#coding:utf8
'''
Created on 2013-11-5

@author: chenghong
'''
from selenium import webdriver
from Page.login import Login


def getUserLogin(driver,url,user,pwd):
    '''
    预制用例：用户登陆
    '''
    
    UserLogin = Login(driver,url)
    
    try:
        UserLogin.input_usr(user)
        UserLogin.input_pwd(pwd)
        UserLogin.click_confirm_button()
        print "用户登陆成功"
    except Exception as e:
        return e