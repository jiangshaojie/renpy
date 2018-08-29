# -*- coding: utf-8 -*-
import hashlib
import requests
from log import logger
import json
class gensign(object):
    private_key='d082205acf33c732c20411f8391dcd2b'
    msg= {"assets_id": "ZC0150",
             "data": "{\"repayment_schedule_list\":[{\"repayment_money\":\"8999.00\",\"repayment_interests\":\"97.49\",\"repayment_time\":\"2018-09-13\",\"periods\":\"1\",\"repayment_service_charge\":\"0.00\",\"current_period\":\"9096.49\"}],\"lender_list\":[],\"loan_info\":{\"order_no\":\"ZC20180810164816485799\",\"financing_order_no\":\"10test53090\",\"financing_name\":\"金蛋理财\",\"loan_money\":\"10000.00\",\"loan_status\":\"1\",\"create_time\":\"2018-08-24\",\"`\":\"2018-08-10\",\"interest_end\":\"2018-09-10\",\"periods\":1,\"repayment_method\":2,\"borrow_deadline\":30,\"deadline_unit\":1,\"interest_rate\":\"13.00\",\"interest_rate_type\":2,\"total_principal\":\"10000.00\",\"total_interests\":\"404.40\",\"total_service_charge\":\"0.00\",\"total_money\":\"10404.40\"},\"base_info\":{\"assets_order_no\":\"2018081418364600000054\",\"product_id\":\"ZC0150-01\",\"order_status\":70}}",
         "time": 1533898087, "sign": "d999736b7ba8f9ba8282ba4ccfcca51e"}
    def gennoticesign(self):
        s=self.msg["assets_id"]+self.msg["time"].__str__()+self.private_key+self.msg["data"]
        # 创建md5对象
        hl = hashlib.md5()
        hl.update(s.encode(encoding='utf-8'))
        print(s)
        # print(hl.hexdigest().upper())
        rs=hl.hexdigest()
        # rs=hl.digest()
        self.msg["sign"]=rs
        print(rs)
        # print(json.dumps(self.msg))
        print(self.msg)
        return rs

    def postmsg(self):
        url='http://10.31.153.170:8087/notice/loan/jd'
        headers=dict()
        headers['Content-Type']='application/json'
        rs=requests.post(url=url,data=self.msg,headers=headers)
        logger.info(rs)
        if rs.status_code=='200':
            logger.info("回调结果： "+rs.text)


if __name__=='__main__':
    a=gensign()
    a.gennoticesign()
#     assets_order_no="""
#     2018081414131600000003
# 2018081414131700000004
# 2018081414131700000005
# 2018081414131700000006
# 2018081414131700000007
# 2018081414131700000008
# 2018081414131800000009
# 2018081414131800000010
#     """
#
#     for i in assets_order_no.splitlines():
#          if i.strip().__len__()>0:
#             print(i.strip())
    # pass