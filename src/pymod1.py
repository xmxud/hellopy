# -*- coding: utf-8 -*-
'''
Created on 2015年1月6日

@author: xiaoman
'''
import platform;
import time;
class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        print "Current platform.uname() in Ecplise+PyDev=", platform.uname();


localtime = time.localtime(time.time())
print "Local current time :", localtime
