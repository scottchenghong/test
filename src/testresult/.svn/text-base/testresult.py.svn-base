# -*- coding:utf-8
'''
Created on Jun 25, 2013

@author: chenghong
'''

import HTMLTestRunner

def testreport():
    '''
    #生成测试报告文件
    '''
    
    filename = 'D:\\testresult.html'
    fp = open(filename,'a')
    
    runner = HTMLTestRunner.HTMLTestRunner(
                                           stream = fp,
                                           title = '测试结果',
                                           description = '测试报告'
                                           )
    return runner