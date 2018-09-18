# -*- coding: utf-8 -*-
import time, random
import requests
from log import logger
import json
from dk.AESECB import AESECB
import hashlib
from dk.utils.signature import gensin
class sharepay():
    # 线上地址
    # url = 'http://innerpaycenter.shanyishanmei.com/'
    #线下地址
    url='http://172.20.94.96:8800/'
    preorderbody={
      "ucid":"885743499612262400",
      "source":"50001",
      "bizNo":"1535103028935",
      "amount":2,
      "notifyUrl":"https://www.baidu.com/",
      "shareInfoBiz":"""[{"shareService":"renrenche","shareAmount":"1"},{"shareService":"zifang_dg","shareAmount":"1"}]""",
      "operatorId":8706,
      "operatorName":"8706"
    }
    header={
        "Content-Type": "application/json"
    }
    placeorderbody={
            "orderNo": "20180824173105360000000424651248",
            "source": "50001"
        }
    key='r2e0nd9r9fe79nf8e8484ec808264538'
    aes=AESECB(key=key)
    def genencrypt(self):
        # self.preorderbody.pop("signature")
        logger.info("preorderbody"+self.preorderbody.__str__())
        encrypt=self.aes.encrypt(json.dumps(self.preorderbody))
        # print(self.preorderbody)
        return encrypt

    def preorder(self):
        reurl=self.url+'dk/sharePay/preOrder'
        a = str(time.time())
        orderid = a[0:10] + round(random.random() * 1000).__str__()
        self.preorderbody['bizNo']=orderid
        self.preorderbody['signature']=gensin(self.preorderbody)
        # logger.info("验签字符串"+gensin)
        logger.info("分账预下单请求参数"+json.dumps(self.preorderbody))

        re=requests.post(url=reurl,json=self.preorderbody,headers=self.header)
        logger.info('分账预下单 result: '+re.__str__())
        if re.status_code==200:
            logger.info('preorder result: '+re.text)
            print(json.loads(re.text))
            orderNo=json.loads(re.text)["data"]["orderNo"]
            logger.info('preorder orderid: '+orderid)
            logger.info('preorder orderNo: ' + orderNo)
        return orderNo
    def placeorder(self):
        self.placeorderbody["orderNo"]=self.preorder()
        self.placeorderbody['signature']=gensin(self.placeorderbody)
        reurl=self.url+'dk/sharePay/placeOrder'
        logger.info("分账下单请求参数"+json.dumps(self.placeorderbody))
        re = requests.post(url=reurl,json=self.placeorderbody, headers=self.header)
        logger.info('分账下单  result: ' + re.__str__())
        if re.status_code == 200 and json.loads(re.text)["status"]==0:
            logger.info('placeorder success')
if __name__=='__main__':
    logger.info("start..............")
    a=sharepay()
    # a.preorder()
    a.placeorder()
