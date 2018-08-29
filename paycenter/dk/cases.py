#encoding:utf-8
from log import logger
logger.info("start..............")

def nocards():
    #ucid无签约卡
    a = orders()
    # a.placeorder()
    a.preorderbody["ucid"] = 1029699755455811584
    a.preorder()