#!/usr/bin/python
import threading
import time
import logging
import logging.config
logging.config.fileConfig('logging.conf')
# create logger
logger = logging.getLogger('simpleExample')
# Define a function for the thread
def print_time( threadName, delay):
 logger.debug('thread 1 call print_time function body')
 count = 0
 logger.debug('count:%s',count)