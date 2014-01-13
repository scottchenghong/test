#-*- coding: utf-8 -*-
#-------------------------------------------
# Name:     encryption.py
# Purpose:  
# Author:           wangxinjun
# Create:           20/03/2013
# Copyright:        (c) Administrator   2013
#Licence:           <Licence 2>
#--------------------------------------------



if __name__ == '__main__':
    fname="excel\\aa.xls"
    tdata=td.CaseExcel(fname)
    print(tdata.getArglist())
    res=tdata.setTestResault(3,'2')
    if res:
        print('插入成功')
    else:
        print('插入失败')