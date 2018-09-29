# -*- coding: utf-8 -*-
import time, random
import requests
from log import logger
import json
from dk.AESECB import AESECB
import hashlib
class sharepay():
    key="r2e0nd9r9fe79nf8e8484ec808264538"
    url='http://172.20.94.97:8088/'
    preorderbody={
      "ucid":"1032588592796405760",
      "source":"50001",
      "bizNo":"1535103028935",
      "amount":30000,
      "notifyUrl":"https://www.baidu.com/",
      "shareInfoBiz":"""[{"shareService":"renrenche","shareAmount":"10000"},{"shareService":"zifang_dg","shareAmount":"20000"}]""",
      "settleFeeItem":"",
      "operatorId":8706,
      "operatorName":"8706",
      "certNo": "130682199010296931"
    }
    header={
        "Content-Type": "application/json"
    }
    placeorderbody={
            "orderNo": "20180824173105360000000424651248",
            "source": "50001"
        }
    aes=AESECB(key=key)
    def preorder(self):
        reurl=self.url+'dk/sharePay/preOrder'
        a = str(time.time())
        orderid = a[0:10] + round(random.random() * 1000).__str__()
        self.preorderbody['bizNo']=orderid
        # self.preorderbody['signature']=self.gensin()
        # print(json.dumps(self.preorderbody))
        logger.info("分账预下单请求参数："+self.preorderbody.__str__())
        re=requests.post(url=reurl,json=self.preorderbody,headers=self.header)
        logger.info('分账预下单 result: '+re.__str__())
        if re.status_code==200:
            logger.info('分账预下单 result: '+re.text)
            print(json.loads(re.text))
            orderNo=json.loads(re.text)["data"]["orderNo"]
            logger.info('分账预下单 orderid: '+orderid)
            logger.info('分账预下单 orderNo: ' + orderNo)
        return orderNo
    def placeorder(self):
        self.placeorderbody["orderNo"]=self.preorder()
        reurl=self.url+'dk/sharePay/placeOrder'
        logger.info("分账下单请求参数： "+self.placeorderbody.__str__())
        re = requests.post(url=reurl,json=self.placeorderbody, headers=self.header)
        logger.info('分账下单 result: ' + re.text.__str__())
        if re.status_code == 200 and json.loads(re.text)["status"]==0:
            logger.info('placeorder success')
if __name__=='__main__':
    logger.info("start..............")
    a=sharepay()
    # a.preorder()
    a.placeorder()
    # a.preorder()