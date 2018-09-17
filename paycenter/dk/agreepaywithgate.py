# -*- coding: utf-8 -*-
import time, random
import requests
from log import logger
import json
import hashlib
class apreepay():
    key = "r2e0nd9r9fe79nf8e8484ec808264538"
    #线上地址
    url='http://172.20.94.75:8800/'
    #线下地址
    # url = 'http://172.20.94.96:8800/'
    preorderbody={
      "ucid":"1032160152729423872",
      "source":"50002",
      "bizNo":"1535103028935",
      "amount":30000,
      "notifyUrl":"https://www.baidu.com/",
      "operatorId":8706,
      "operatorName":"8706"
    }
    header={
        "Content-Type": "application/json"
    }
    placeorderbody={
            "orderNo": "20180824173105360000000424651248",
            "source": "50002"
        }
    def gensin(self,signparamer):
        s=list()
        paramers=''
        for k,v in signparamer.items():
            s.append(k+"="+v.__str__())
        s.sort()
        for i in s:
            paramers=paramers+i+'&'
        paramers=paramers+"key"+"="+self.key
        hl = hashlib.md5()
        hl.update(paramers.encode(encoding='utf-8'))
        logger.info("验签字符串"+paramers)
        print(paramers)
        print(hl.hexdigest())
        return hl.hexdigest()
    def preorder(self):
        reurl=self.url+'dk/agreePay/preOrder'
        a = str(time.time())
        orderid = a[0:10] + round(random.random() * 1000).__str__()
        self.preorderbody['bizNo']=orderid
        self.preorderbody['signature']=self.gensin(self.preorderbody)
        logger.info("预下单请求参数"+self.preorderbody.__str__())
        re=requests.post(url=reurl,json=self.preorderbody,headers=self.header)
        logger.info('preorder result: '+re.__str__())
        if re.status_code==200:
            logger.info('preorder result: '+re.text)
            print(json.loads(re.text))
            orderNo=json.loads(re.text)["data"]["orderNo"]
            logger.info('preorder orderid: '+orderid)
            logger.info('preorder orderNo: ' + orderNo)
        return orderNo
    def placeorder(self):
        self.placeorderbody["orderNo"]=self.preorder()
        reurl=self.url+'dk/agreePay/placeOrder'
        self.placeorderbody['signature'] = self.gensin(self.placeorderbody)
        logger.info("下单请求参数"+self.placeorderbody.__str__())
        re = requests.post(url=reurl,json=self.placeorderbody, headers=self.header)
        logger.info('preorder result: ' + re.__str__())
        if re.status_code == 200 and json.loads(re.text)["status"]==0:
            logger.info('placeorder success')
if __name__=='__main__':
    logger.info("start..............")
    a=apreepay()
    a.placeorder()
    # a.preorder()