# -*- coding: utf-8 -*-
import configparser
import os
class readconf():

    def __init__(self):
        self.config = configparser.ConfigParser()
        # configname = 'config.conf'
        # self.configname=os.path.curdir.join('config')
        self.configname=os.getcwd()+'\config'
        self.config.read(self.configname, encoding="utf-8")

    def getConfig(self,section,key):
        return self.config.get(section,key)
    def getsections(self,section):
        return dict(self.config.items(section))

if __name__=='__main__':
    a=readconf()
    print(a.configname)
    print(a.getConfig('rrcp-bgtwfront-api','url'))
    print(a.getsections('rrcp-bgtwfront-api'))