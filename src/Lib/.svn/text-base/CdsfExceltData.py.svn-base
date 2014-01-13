# -*- coding: utf-8 -*-
#-------------------------------------------
# Name:     TestData.py
# Purpose:  解析excel数据，为外部程序提供数据
# Author:           wangxinjun
# Create:           08/04/2013
# Copyright:        (c) Administrator   2013
#--------------------------------------------

import  xlrd
import  os
import  win32com.client
from    win32com.client import  Dispatch

class    NoFoundExcelFile(Exception):pass
class    ExcelContentIsNull(Exception):pass

class CaseExcel(object):
    '''
        Excel解析，返回文件中参数，
    '''
    def __init__(self,fname):
            self.fname=fname
    
    def openExcel(self):
        '''
        打开EXCEL文件返回xlrd的Book对象
        '''  
        try:
            self.data=xlrd.open_workbook(self.fname,ragged_rows=0)
            return    self.data
        except IOError:
            raise NoFoundExcelFile('No such file or directory: %s'%(self.fname,))
        except  Exception as e:
            raise e
            
    def getArgNameList(self):
        '''
        获取EXCEL模板中参数名列表
        '''
        table=self.openExcel().sheets()[0]
        nrows=table.nrows
        ncols=table.ncols
        if nrows or ncols>0:
            argNameList=[]
            argsCount=table.cell(1,1).value#获取模板内cell(1，1)固定的参数个数
            for i in range(1,int(argsCount)+1):#循环获取参数名称所在列
                argNameList.append(table.cell(2,i).value)
            argNameList.append('row')
            return argNameList
        else:
            raise ExcelContentIsNull('Excel Content Is Null')
 
    def getNcols(self):
        '''
        获取EXCEL中总行数
        '''
        table=self.openExcel().sheets()[0]
        nrows=table.nrows
        return nrows
    
    def getArgValueList(self):
        '''
        获取参数对应的值列表
        '''
        ParValueList=[]
        nrows=self.getNcols()
        for i in range(3,nrows):
            table=self.openExcel().sheets()[0]
            argsCount=int(table.cell(1,1).value)+1
            caseRowList=table.row_values(i)
            parValue=caseRowList[1:argsCount]#利用列表切片操作，去除不需要的数据
            parValue.append(str(i))
            ParValueList.append(parValue)
        return ParValueList
    
    def getArglist(self):
        '''
        组装参数名列表和参数值列表，并列表形式返回
        '''
        argList=[]
        ParValueList=self.getArgValueList()
        argNameList=self.getArgNameList()
        leng=len(ParValueList)
        for i in range(0,leng):
            argList.append(dict(zip(argNameList,ParValueList[i])))#组合返回的参数名列表和参数值列表
        return argList
    
    def setTestResault(self,row,resault):
        '''
        更新Excel测试用例Test Result，返回值0：更新失败，返回值1：成功
        '''
        xlsApp=Dispatch('Excel.Application')
        xlsApp.Visible=0
        col=7
        xlspath=os.path.abspath(self.fname)
        try:
            xlsBook=xlsApp.WorkBooks.Open(xlspath)
        except IOError:
            raise NoFoundExcelFile('No such file or directory: %s'%(self.fname,))
        except Exception as e:
            raise e
        xlsCurSheet=xlsBook.WorkSheets('sheet1')
        xlsCurSheet.Cells(row+1,col).Value=resault
        try:
            xlsBook.Save()
            xlsBook.Close(SaveChanges=1)
            xlsApp.Quit()
            return 1
        except Exception as e:
            return 0
        
    