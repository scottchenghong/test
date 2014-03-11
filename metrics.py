#coding:utf8

'''
Created on 2014-3-4

@author: chenghong
'''

import time
import random
import urllib,urllib2
import msg_pb2

class metrics(object):
    '''
    根据metrics协议标准构造valuelist数据，并通过post接口循环发数据
    '''
    
    def get_body(self,metrics,value):
        '''
        构造数据
        '''
        metrics.timestamp = int(time.time())
        metrics.value = float(value)
        metrics.localid = random.randint(0,9)
        
        return metrics
        
    def post(self,url):
        '''
        序列化，并循环发送post请求
        '''
        url = 'http://%s/queue/1234567890/metrics' %(url)
        valuelist = [0,0.2,0.4,0.6,0.8,1.0,0.8,0.6,0.4,0.2]
        
        StorageRequest = msg_pb2.StorageRequest()
        
        while 1:
            for value in valuelist:
                
                print self.get_body(StorageRequest.metrics.add(),value)
                #序列化
                msgs = StorageRequest.SerializeToString()
                
                #发送post请求
                try:
                    req = urllib2.Request(url,msgs)
                    urllib2.urlopen(req)
                except Exception as ex:
                    raise ex
                time.sleep(1)
            
                #clear list
                StorageRequest.Clear()
        
        return 1
    
    
if __name__ == '__main__':
    url = '192.168.1.133:7880'
    metrics = metrics()

    metrics.post(url)

 
