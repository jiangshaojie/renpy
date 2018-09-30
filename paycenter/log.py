# -*- coding: utf-8 -*-


import logging
import sys
import os
import time


#获取logger实例
logger=logging.getLogger("AppName")
# logger=logging.getLogger()

#日志格式
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
# formatter=logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

#文本日志相关设置
#创建日志文件夹函数
def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path

#日志文件夹
log_dir_name = "logs"
#日志文件名，根据日期自动生成
log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + os.sep + log_dir_name
print(log_file_folder)
make_dir(log_file_folder)
# print(make_dir(log_file_folder))
log_file_str = log_file_folder + os.sep + log_file_name

file_handler = logging.FileHandler(log_file_str, encoding='UTF-8')

file_handler.setFormatter(logging_format)




#控制台日志

consle_handler=logging.StreamHandler(sys.stdout)
consle_handler.formatter=logging_format

#为Logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(consle_handler)

#指定级别
logger.setLevel(logging.INFO)
