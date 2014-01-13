# -*- coding:utf-8 -*-
'''
Created on 2013-11-12


@author: Cliu
'''

def PageSqlCompare(pageData,sqlData):
    """
    if pageData Equal with sqlData,return 1,else return 0
    """
    #print pageData,sqlData
    Equal = 1
    for i in range(0,len(pageData)):
        for j in range(0,len(pageData[i])):
            print pageData[i][j],sqlData[i][j]
            if pageData[i][j] != sqlData[i][j]:
                Equal = 0 
                break 
    return Equal