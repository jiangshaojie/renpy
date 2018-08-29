# -*- coding: utf-8 -*-
import time
import random
import hashlib
import json
import datetime
from log import logger
import requests
from financingmng.utils.RDSWrapper import RDS
class common(object):

    header = """
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-cn
    Cookie: SESSION=c4554aca-ea4b-4fe4-a46b-1aead91348c4
    """
    orderid=''
    fundPayNo=''
    url='http://10.31.153.170:8087/api/'
    def __init__(self,preparamters,payparamters):
        self.preparamters=preparamters
        self.payparamters=payparamters
    def headers_to_dict(self,headers):
        # 将字符串转换成字典
        headers = headers.split('\n')
        header = dict()
        for i in headers:
            h = i.strip()
            if h:
                k, v = h.split(":", 1)
                header[k] = v.strip()
        return header

    def genSign(self,orderId,busiLine,createTime):
        password_off = "Icy35a5R"
        password_online = "cGXu5S6Q"
        s = orderId + "|" + busiLine + "|" + createTime + "|" + password_off
        logger.info(s)
        # 创建md5对象
        hl = hashlib.md5()
        hl.update(s.encode(encoding='utf-8'))
        signature=hl.hexdigest().upper()
        logger.info(signature)
        return signature


    def preOrder(self):
        a = str(time.time())
        self.orderid=a[0:10] + round(random.random() * 1000).__str__()
        self.preparamters['orderId']=self.orderid
        creattime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.preparamters['createTime']=creattime
        self.preparamters['applyTime']=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sign=self.genSign(self.orderid,self.preparamters.get('busiLine'),creattime)
        self.preparamters['sign']=sign
        logger.info(self.preparamters)
        preurl=self.url+'preOrderV1'
        logger.info(preurl)
        rl=requests.put(preurl,json=self.preparamters,headers=self.headers_to_dict(self.header))
        # rl.
        logger.info(rl)
        if rl.status_code==200:
            logger.info(rl.text)
            result=json.loads(rl.text)
            if result["status"] == 10000:
                self.fundPayNo=result["data"]["fundPayNo"]

            logger.info("预下单结果： "+rl.text)

    def payOrder(self):
        # a = str(time.time())
        creattime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.payparamters["createTime"]=creattime
        self.payparamters["orderId"]=self.orderid
        sign=self.genSign(self.orderid,self.payparamters['busiLine'],creattime)
        self.payparamters["sign"]=sign
        self.payparamters["fundPayNo"]=self.fundPayNo
        now_time = datetime.datetime.now()
        t_time = now_time + datetime.timedelta(days=+1)
        t_time_yr = t_time.strftime("%Y-%m-%d %H:%M:%S")
        self.payparamters['exceptPaymentTime']=t_time_yr
        logger.info(payparamters)
        payurl=self.url+'payOrder'
        print(payurl)
        rl = requests.post(payurl, json=self.payparamters, headers=self.headers_to_dict(self.header))
        logger.info(rl)
        if rl.status_code == 200:
            logger.info("下单结果： "+rl.text)







if __name__=='__main__':
    # applyTime,createTime,orderId,sign
    preparamters={
    "applyPaymentAmount":2999900,
    "applyUserId":"21977",
    "applyUserName":"shanpao666",
    "busiLine":"20000",
    "busiLineName":"包卖-C1",
    "contractAmount":2,
    "feeType":3,
    "paymentRatio":100,
    "remark":"线上测试",
    "userName":"哈哈",
    "userIdCardNo":"532326198507231775",
    "mobileNum":"13694940707",
    "bankNo":"6228480028135906754",
    "ucid":"1029699755455811584",
    "parkingLotId": "36"

    }
    # exceptPaymentTime,createTime,orderId,sign,fundPayNo
    payparamters={
    "applyPaymentAmount":2999900,
    "approvalProcess":[],
    "bankCode":"104100005619",
    "busiLine":"20000",
    "busiLineName":"包卖-C1",
    "carSourceInformation":"1a1a1aa1a1a1",
    "city":"北京",
    "collectionAccountBankNo":"6212260200134579313",
    "collectionAccountCity":"北京",
    "collectionAccountName":"于文胜",
    "collectionIDCardNo":"111111111111",
    "collectionAccountPhone":"13810148279",
    "collectionAccountProvince":"北京",
    "collectionBankBranch":"昌平龙泽支行",
    "collectionBankName":"中国工商银行",
    "exceptPaymentTime":"2018-07-21 00:00:00",
    "paymentType":2,
    "sign":"80C0502B7607BE766B693C827F31F919"
}
    #
    a=common(preparamters,payparamters)

    # a.preOrder()
    #  a.payOrder()
    # print("订单号： "+a.preparamters['orderId'])
    amounts=[10001100]
    # amounts = [50000]
    with open("order.text",'w') as file:
        for i in amounts:
            a.preparamters["applyPaymentAmount"]=i
            a.payparamters["applyPaymentAmount"]=i
            a.preOrder()
            a.payOrder()
            logger.info("订单号： " + a.preparamters['orderId'])
            file.write(a.preparamters['orderId'])
            file.write(',')
        # print(a.preparamters)