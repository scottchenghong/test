# -*- coding:utf8 -*-

'''
Created on Jun 25, 2013

@author: chenghong
'''

from testresult.testresult import testreport
import discover

def controller():
    
    testSuite = discover.defaultTestLoader.discover("TestCase")
    
    return testreport().run(testSuite)

if __name__ == '__main__':
    
    controller()