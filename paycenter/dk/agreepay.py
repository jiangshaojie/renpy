# -*- coding: utf-8 -*-
import time, random
import requests
from log import logger
import json
class apreepay():
    url='http://172.20.94.97:8088/'
    preorderbody={
      "ucid":"1032588592796405760",
      "source":"50001",
      "bizNo":"1535103028935",
      "amount":30000,
      "notifyUrl":"https://www.baidu.com/",
      "operatorId":8706,
      "operatorName":"8706",
      "certNo":"142427199307225710"
    }
    header={
        "Content-Type": "application/json"
    }
    placeorderbody={
            "orderNo": "20180824173105360000000424651248",
            "source": "50001"
        }
    def preorder(self):
        reurl=self.url+'dk/agreePay/preOrder'
        a = str(time.time())
        orderid = a[0:10] + round(random.random() * 1000).__str__()
        self.preorderbody['bizNo']=orderid
        logger.info("预下单请求参数"+self.preorderbody.__str__())
        re=requests.post(url=reurl,json=self.preorderbody,headers=self.header)
        logger.info('预下单返回结果 : '+re.__str__())
        if re.status_code==200:
            logger.info('预下单返回结果: '+re.text)
            # print(json.loads(re.text))
            orderNo=json.loads(re.text)["data"]["orderNo"]
            logger.info('preorder orderid: '+orderid)
            logger.info('preorder orderNo: ' + orderNo)
        return orderNo
    def placeorder(self):
        self.placeorderbody["orderNo"]=self.preorder()
        reurl=self.url+'dk/agreePay/placeOrder'
        logger.info("下单请求参数"+self.placeorderbody.__str__())
        re = requests.post(url=reurl,json=self.placeorderbody, headers=self.header)
        logger.info('下单返回结果 result: ' + re.__str__())
        logger.info('下单返回结果 result: ' + re.text)
        if re.status_code == 200 and json.loads(re.text)["status"]==0:
            logger.info('placeorder success')
if __name__=='__main__':
    logger.info("start..............")
    a=apreepay()
    a.placeorder()
    # a.preorder()