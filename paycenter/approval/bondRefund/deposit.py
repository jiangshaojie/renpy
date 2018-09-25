# coding=utf-8
import hashlib, time, requests
# from http_request import req
import requests
from  log import logger
def en_token():
	# MD5(key+timestamp)+timestamp
	key = '56dfd834f8d23c98dc64892dbdcdf105'
	timestamp = str(int((time.time()*1000)))
	refund = key + timestamp
	# 创建md5对象
	hl = hashlib.md5()
	hl.update(refund.encode(encoding='utf-8'))
	return hl.hexdigest() + timestamp

def create(host, rrc_user_id):
    #创建车商退款申请
        create_url = "http://{}:8090/refund/create".format(host)
        data = {
            "token": en_token(),
            "type":"9",
            "source":"10013",
            "order_id":str(int((time.time()*1000))),
            "order_city":"北京",
            "rrc_user_id": rrc_user_id,
            "rrc_user_name":"车商001",
            "user_id":"100216",
            "user_name":"柳栋杰",
            "remark":"测试",
            "fee":{
                "c2b_deposit":0.1
            },
            "account":{
                "number":"7234567892345678",
                "bank":"招商银行",
                "province":"北京",
                "city":"北京",
                "phone":"18810936553",
                "sub_branch":"望京支行",
                "holder":"测试人员"
            }
        }
        header = {
            "Content-Type": "application/json"
        }

        # req("post", create_url, data)
        logger.info("退款申请订单号: "+data['order_id'].__str__())
        result=requests.post(create_url,json=data,headers=header)
        logger.info("退款申请返回结果："+result.status_code,"    ",result.text)
        # pass
if __name__ == '__main__':
	host = "10.81.35.44"
	rrc_user_id = "db8b543ab401000"
	create(host, rrc_user_id)