# -*- coding: utf-8 -*-


import logging
import sys
import os


#获取logger实例
logger=logging.getLogger("AppName")

formatter=logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

#文件日志
logfile="test.log"
if os.path.exists("logs/test.log"):
    pass
else:
    if os.path.exists("logs/"):
        os.chdir("logs/")
        open(logfile, "w")
    else:
        os.mkdir("logs",777)
        open(logfile,"w")
file_handler=logging.FileHandler(logfile,encoding="utf-8")
file_handler.setFormatter(formatter)

#控制台日志

consle_handler=logging.StreamHandler(sys.stdout)
consle_handler.formatter=formatter

#为Logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(consle_handler)

#指定级别
logger.setLevel(logging.INFO)
