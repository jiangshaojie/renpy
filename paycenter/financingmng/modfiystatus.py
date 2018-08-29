# -*- coding: utf-8 -*-
import requests
from financingmng.utils.RDSWrapper import RDS
from log import logger
import time
class modfiystatus():
    def get_ids(self,orderid):
        rds = RDS(db="finance")
        sql = "SELECT approval_id FROM approval_order WHERE order_id='%s'" % orderid
        logger.info('查询approval_id sql： '+sql.__str__())
        approval_id = rds.select(sql)[0]["approval_id"]
        sql2 = "SELECT	process_instance_id FROM approval_form WHERE id=%s" % approval_id
        logger.info('查询 process_id sql: '+sql2.__str__())
        process_id = rds.select(sql2)[0]["process_instance_id"]
        return approval_id, process_id

    def move_dot(self,orderid):
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        process_id = self.get_ids(orderid)[-1]
        url = "http://10.31.153.170:8090/check/task/move?processInstanceId={}&taskDefKey=end&token=yhgajh6527t3bdnjhgs".format(
            process_id)
        try:
            print("process_id:%s" % process_id)
            res = requests.post(url, headers=headers)
            logger.info('move_dot: '+res.text)
            return res.json()
        except Exception as e:
            print(e.message)
            logger.info(e.message)

    def push_mesg(self,orderid):
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        url = "http://10.31.153.170:8090/refund/sendMessageBus"
        approval_id = self.get_ids(orderid)[0]
        data = {"approvalIds": approval_id, "type": "7"}
        try:
            # print("approval_id:%s" % approval_id)
            logger.info('pubsh_mesg approval_id:%s' % approval_id)
            res = requests.put(url, headers=headers, json=data)
            logger.info('push_mesg: ' + res.text)
            return res.json()
        except Exception as e:
            print(e.message)
            logger.info(e.message)

if __name__ == "__main__":
    modfiy=modfiystatus()
    orderlist=list()
    with open("order.text",'r') as orderfile:
        re=orderfile.readlines()
        for i in re:
            orderlist=i.strip().split(',')[:-1]
    logger.info("订单list: "+orderlist.__str__())
    print(orderlist)
    # orders=['1534573861306']
    for orderid in orderlist:
        modfiy.move_dot(orderid)
        time.sleep(1)
        modfiy.push_mesg(orderid)