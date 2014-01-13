#coding:utf8

'''
Created on 2013-11-6

@author: chenghong
'''
from smtplib import SMTP
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart


def sendMail(host,port,fromMail, toMail, msg):
    
    '''
       发送邮件
    '''
    
    smtp = SMTP()
    
    try:
        smtp.connect( host, port)
        print '11'
        smtp.login( 'chenghong@cdsf.com', 'chengHONG369')
        print '22'
    
        smtp.sendmail(fromMail, toMail, msg.as_string())
        print '33'
    except Exception as e:
        print e
    finally:
        smtp.close()
        print 'over'
    


if __name__ == '__main__':
    
    
    host = 'smtp.exmail.qq.com'
    port = '25'
    fromMail = 'chenghong@cdsf.com'
    toMailList = ['liuchengshuang@cdsf.com',
              'wangzhenzhong@cdsf.com',
              'wujie@cdsf.com',
              'wupengjian@cdsf.com',
              'liaoyongjun@cdsf.com',
              '553218391@qq.com']
    
    #附件实例
    msg = MIMEMultipart()
    
    msg['Subject'] = ' The Newest TestResultReport'
    msg['from'] = fromMail
    msg['to'] = ';'.join(toMailList)
    
    
    #发送HTML测试报告附件
    msgFile = MIMEText(open(r'D:\\testresult.html','rb').read(),'base64','gb2312')
    msgFile["Content-Type"] = 'application/octet-stream'
    msgFile["Content-Disposition"] = 'attachment; filename="testresult.html'
    msg.attach(msgFile)
    print 'file ok'
    
    sendMail(host,port,fromMail, toMailList, msg)