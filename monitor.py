# coding:utf8

'''
Created on 2014-2-27

@author: chenghong
'''

import os
import re


'''
执行redis-benchmark并发测试命令；
统计在该并发请求下，响应时间的最大值、最小值、平均值；
分类别统计响应时间对应完成请求的百分比情况
'''

def execCommand(host,port,concurrency,requests):
    '''
    执行测试命令，返回测试结果
    @param concurrency: 并发数
    @param requests: 请求数
    @return: result 返回值为dict
    '''
    percentlist = []
    mslist = []
    
    command = 'redis-benchmark -h %s -p %s -t get -d 20 -c %d -n %d' %(host,port,concurrency,requests)

    #execute command
    result = os.popen(command).readlines()[6:-3]
    
    #解析测试结果文件中的响应时间
    for element in result:
        #解析每个元素str，依照'<='进行切片
        new = element.split('<=')
        #将new列表中的百分比元素转化为float，添加到percentlist
        percentlist.append(float(new[0].split('%')[0]))
        #将new列表中的时间转化为int,添加到mslist
        mslist.append(int(new[1].split(' ')[1]))
    
    #两个list进行组合成dict
    result = dict(zip(mslist,percentlist))
    
    return result
    
def countResult(result):
    '''
    分别计算最大值、最小值、平均值
    @param result: 性能测试结果
    @return: 返回最值dict,keys = ['max','min','avg']
    '''
    mstimelist = []
    countdic = {}
    
    #遍历测试结果list
    for key in result:
        mstimelist.append(key)

    #计算最大值、最小值、平均值
    countdic['max'] = max(mstimelist)
    countdic['min'] = min(mstimelist)
    countdic['avg'] = mstimelist[len(mstimelist)//2]

    return countdic

def getMinTime(array,target):
    '''
    获取最接近目标时间的数值
    @param arry: dict
    @param target: 目标时间，即类别时间
    @return: 返回最接近目标时间的dict,key为ms,value为百分比
    '''
    typedict = {}
    comparedict = {}
    mslist = []
    
    #遍历字典，获取每个key与target的绝对值，并组合成心的dict-comparedict
    for ms in array:
        comparedict[abs(target - ms)] = ms
    
    #获取比较绝对值字典中的最小值
    for absvalue in comparedict:
        mslist.append(absvalue)
    
    #找出最小的绝对值    
    ms = comparedict[min(mslist)]
    #添加到dict
    typedict[ms] = array[ms]
         
    return typedict

def sort(init,total,add,array):
    '''
    对性能结果进行分类统计
    @param inittime: init ms
    @param totaltime: the end ms
    @param addtime: add ms-time every time
    @return: 返回某一段ms区间每个增长点的响应百分比dict,key为ms,value为百分比
    '''
    result = {}
    newresult = {}
    result = getMinTime(array,init)
    
    #某一段时间内的响应时间变化
    for mstime in range(init,total,add):
        result = dict(result,**getMinTime(array,mstime))
    
    #根据dict的key进行排序
    keys = result.keys()
    keys.sort()
    
    newresult[keys[0]] = result[keys[0]]
    for key in keys[1:]:
#        print '当前key:',key,'上一个key:',keys[keys.index(key)-1]
        newresult[key] = result[key] - result[keys[keys.index(key)-1]]
    
    return newresult
    
def main():
    #host and port
    host = '127.0.0.1'
    port = 6379
    
    #循环执行
    initconcurrency = 100
    endconcurrency = 800
    addconcurrency = 100
    
    
    for concurrency in range(initconcurrency,endconcurrency,addconcurrency):
        #提交并发数到redis
        command = 'redis-cli -h %s -p %d set monitor.concurrency %s' %(host,port,concurrency)
        os.popen(command)
        print 'concurrency:\n',os.popen('redis-cli get monitor.concurrency').read()
        
        #执行测试命令，返回时间结果
        result = execCommand(host,port,concurrency,concurrency)
        #计算最值
        limitdict = countResult(result)
        #分类统计
        sortdict = sort(100,500,100,result)
        
        #提交最值到redis
        max = limitdict['max']
        min = limitdict['min']
        avg = limitdict['avg']
        
        command = 'redis-cli -h %s -p %d hmset monitor.latency.quecy.values max %d avg %d min %d' %(host,port,max,avg,min)
        os.popen(command)
        print 'limitresult:\n',os.popen('redis-cli hgetall monitor.latency.quecy.values').read()
        
        #提交分类统计结果到redis
        for key in sortdict:
            command = 'redis-cli -h %s -p %d hmset monitor.latency.quecy.scatter %d %d' %(host,port,key,sortdict[key])
            os.popen(command)
        print 'sortresult:\n',os.popen('redis-cli hgetall monitor.latency.quecy.scatter')
            
        
if __name__ == '__main__':
    main()
