# import time,random
# a = str(time.time())
# orderid=a[0:10] + round(random.random() * 1000).__str__()
# print(orderid)
import json
a='{"status":0,"err_msg":null,"data":{"orderNo":"20180827170141484000004787429058"},"total":0}'
b=json.loads(a)
print(type(b))
