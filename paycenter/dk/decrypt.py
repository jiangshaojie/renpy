import json
import hashlib
s={'ucid': '1032588592796405760', 'source': '50001', 'bizNo': '1536723280704', 'amount': 20000, 'notifyUrl': 'https://www.baidu.com/', 'shareInfoBiz': '[{"shareService":"renrenche","shareAmount":"1"},{"shareService":"zifang_dg","shareAmount":"2"}]', 'settleFeeItem': '', 'operatorId': 8706, 'operatorName': '8706'}

key='r2e0nd9r9fe79nf8e8484ec808264538'
paramstr=list()
for k,v in s.items():
    paramstr.append(k+"="+v.__str__()+"&")
paramstr.sort()
str=''
for i in paramstr:
    str=str+i
str=str+"key="+key
# print(paramstr)
print(str)
hl = hashlib.md5()
hl.update(str.encode("utf-8"))
# logger.info("验签字符串"+s)
print(hl.hexdigest())