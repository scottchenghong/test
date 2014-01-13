#coding:utf8

'''
Created on 2013-11-5

@author: chenghong
'''

import MySQLdb

class Mysql():
    '''
    '''
    def __init__(self,dbHost = '192.168.188.234',dbPort = 3306,dbName = 'platformyun_test',dbUser = 'ygchenghong',dbPwd = 'cdsf2013'):
        '''
        @param dbHost: 数据库主机IP;
        @param dbPort: 数据库主机端口号，默认一般为3306;
        @param dbName: 数据库名称
        @param dbUser: 数据库用户名称
        @param dbPwd:  数据库用户对应的密码   
        '''
        self.dbHost = dbHost
        self.dbPort = dbPort
        self.dbName = dbName
        self.dbUser = dbUser
        self.dbPwd = dbPwd
        
        try:
            self.conn = MySQLdb.connect(self.dbHost,self.dbUser,self.dbPwd,self.dbName,self.dbPort)
            self.cursor = self.conn.cursor()                
        except Exception as e:
            raise e
            
    def selectData(self,sql,num,*args):
        '''
        查询数据
        '''
        try:
            self.cursor.execute('set NAMES utf8')
            self.cursor.execute(sql,args)
            resultsuit = self.cursor.fetchmany(num)
            while resultsuit:
                yield resultsuit
                resultsuit = self.cursor.fetchmany(num)
        except Exception as e:
            raise e
        finally:
            self.closeDb()
         
    def selectAllData(self,sql,*args):
        '''
        查询所有数据
        '''
        try:
            self.cursor.execute('set NAMES utf8')
            self.cursor.execute(sql,args)
            return self.cursor.fetchall()
        except Exception as e:
            return e
        finally:
            self.closeDb()
            
    def closeDb(self):
        self.cursor.close()
        self.conn.close()
            
if __name__ == '__main__':
    
    sql = """select * from CK_DEVICE t where t.DEVICE_ALIAS=%s and t.STATE=%s"""

    
    sql4 ='' 
     
    sql3 ="select * from CK_DOWNLOAD t where t.CREATE_TIME<= DATE_FORMAT(%s,'%%Y-%%m-%%d')"
    sql5 ="""SELECT D2.REALNAME, D2.NAME, D2.DEVICE, D2.CREATE_TIME, D2.LAST_TIME FROM ( SELECT get_channel_manager_realname(C.CHANNEL_ID) AS REALNAME , IF(C.DEVICE_ALIAS IS NULL OR TRIM(C.DEVICE_ALIAS)='',C.DEVICE_CODE,TRIM(C.DEVICE_ALIAS)) as DEVICE, G. NAME, DATE_FORMAT(C.CREATE_TIME,"%%Y-%%m-%%d %%H:%%i:%%s" )AS CREATE_TIME ,IFNULL(DATE_FORMAT(D1.LAST_TIME,"%%Y-%%m-%%d %%H:%%i:%%s" ), '-')AS LAST_TIME FROM CK_DEVICE C LEFT JOIN( SELECT CDS.DEVICE_CODE, MAX(CDS.CREATE_TIME)AS LAST_TIME FROM CK_DEVICE_STATUS CDS WHERE CDS.CREATE_TIME <= STR_TO_DATE(%, "%%Y-%%m-%%d %%H:%%i:%%s") GROUP BY CDS.DEVICE_CODE )D1 ON D1.DEVICE_CODE = C.DEVICE_CODE LEFT JOIN YG_CHANNEL_GD G ON G.ID = C.CHANNEL_ID WHERE C.STATE = 1 AND C.CREATE_TIME <= STR_TO_DATE(%, "%%Y-%%m-%%d %%H:%%i:%%s") ) D2 WHERE 1=1 AND UPPER(D2.DEVICE) LIKE CONCAT('%%',%,'%%') AND LOWER(D2.NAME) LIKE CONCAT('%%',%,'%%') AND LOWER(D2.REALNAME) LIKE CONCAT('%%',%,'%%') ORDER BY REALNAME DESC, NAME DESC limit 0 ,10"""
    sql6 ="""SELECT D2.REALNAME,D2.NAME,D2.DEVICE, D2.CREATE_TIME, D2.LAST_TIME FROM ( SELECT get_channel_manager_realname(C.CHANNEL_ID) AS REALNAME , IF(C.DEVICE_ALIAS IS NULL OR TRIM(C.DEVICE_ALIAS)='',C.DEVICE_CODE,TRIM(C.DEVICE_ALIAS)) as DEVICE, G. NAME, DATE_FORMAT(C.CREATE_TIME,"%%Y-%%m-%%d %%H:%%i:%%s" )AS CREATE_TIME ,IFNULL(DATE_FORMAT(D1.LAST_TIME,"%%Y-%%m-%%d %%H:%%i:%%s" ), '-')AS LAST_TIME FROM CK_DEVICE C LEFT JOIN( SELECT CDS.DEVICE_CODE, MAX(CDS.CREATE_TIME)AS LAST_TIME FROM CK_DEVICE_STATUS CDS WHERE CDS.CREATE_TIME <= STR_TO_DATE(%s, "%%Y-%%m-%%d %%H:%%i:%%s") GROUP BY CDS.DEVICE_CODE )D1 ON D1.DEVICE_CODE = C.DEVICE_CODE LEFT JOIN YG_CHANNEL_GD G ON G.ID = C.CHANNEL_ID WHERE C.STATE = 1 AND C.CREATE_TIME <= STR_TO_DATE(%s, "%%Y-%%m-%%d %%H:%%i:%%s") ) D2 WHERE 1=1 AND UPPER(D2.DEVICE) LIKE CONCAT('%%',%s,'%%') AND LOWER(D2.NAME) LIKE CONCAT('%%',%s,'%%') AND LOWER(D2.REALNAME) LIKE CONCAT('%%',%s,'%%') ORDER BY REALNAME DESC, NAME DESC limit 0 ,10"""
    dateTime = '2013-11-07 17:30:00'
    alise = 'SF0009'
    channlName = '成都'
    print channlName
    realname = '测试'
    print realname
    mysql = Mysql()
    print "test"
    res = mysql.selectAllData(sql6,dateTime,dateTime,alise,channlName,realname)
    print res
    
    
        
        