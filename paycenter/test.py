# -*- coding: utf-8 -*-
# log配置，实现日志自动按日期生成日志文件
import os,time
import logging
# from flask import logging
def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path


log_dir_name = "logs"
log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
log_file_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)) + os.sep + log_dir_name
print(log_file_folder)
make_dir(log_file_folder)
# print(make_dir(log_file_folder))
log_file_str = log_file_folder + os.sep + log_file_name
print(log_file_str)
log_level = logging.INFO

handler = logging.FileHandler(log_file_str, encoding='UTF-8')
handler.setLevel(log_level)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
handler.setFormatter(logging_format)
logger=logging.getLogger()

logger.addHandler(handler)

