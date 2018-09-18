#coding:utf-8
import hashlib

def gensin(singparamer):
    key = "r2e0nd9r9fe79nf8e8484ec808264538"
    s = list()
    paramers = ''
    for k, v in singparamer.items():
        if v!='':
            s.append(k + "=" + v.__str__())
    s.sort()
    for i in s:
        paramers = paramers + i + '&'
    paramers = paramers + "key" + "=" + key
    hl = hashlib.md5()
    hl.update(paramers.encode(encoding='utf-8'))
    # logger.info("验签字符串" + paramers)
    return hl.hexdigest()