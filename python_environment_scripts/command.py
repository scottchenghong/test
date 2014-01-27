#coding:utf8

'''
Created on 2014-1-26

@author: chenghong
'''
import os

def _excute_command(command):
    '''
    find file and setup it
    '''
    return os.system(command)

def kill_process(port):
    '''
    kill process from port
    @param port: port of process
    @return: none 
    '''
    #kill porcess from port
    command = " kill -9 $(lsof -i:%s|tail -1|awk '\"$1\"!=\"\"{print $2}')"%(port)
    
    _excute_command(command)

if __name__ == '__main__':
    kill_process('7272')
