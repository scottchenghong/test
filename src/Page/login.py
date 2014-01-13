# -*- coding:utf-8 -*-
from selenium import webdriver
from Lib.web_control import webControl
class Login(webControl):
    """
    定义全局变量 Control；
    Control变量实例化control对象；
    分别封装输入用户名、密码、确定按钮、错误提示信息等方法；
    """
  
    def input_usr(self,user):       
        '''
        输入用户名
        '''
        self.input_textbox('username',user)        
        
    def input_pwd(self,pwd):
        '''
        输入密码
        '''
        self.input_textbox('password',pwd)
           
    def click_confirm_button(self):
        '''
        点击确定按钮
        '''
        self.click_button("//input[@type='image']")
        
    def errormsg_text(self):
        '''
        显示错误提示信息
        '''
        self.appear_alert()



if __name__ == "__main__":
    user = 'admin'
    pwd = 'cdsf_2012'
    dr = webdriver.Firefox()
    url = 'http://192.168.188.201/yunguan/login'
    try:
        login = Login(dr,url)
    
        login.input_usr(user)
        login.input_pwd(pwd)
    
        login.click_confirm_button()
    except Exception as e:
        print e
    finally:
        import time
        time.sleep(3)
        login.close()
    
    
    
   
    
    
    
