# -*- coding: utf-8 -*-
import hashlib

# 待加密信息
orderId = "20180720006"
busiLine = "20000"
createTime = "2018-07-20 14:26:00"
password_off = "Icy35a5R"
password_online = "cGXu5S6Q"
s = orderId + "|" + busiLine + "|" +createTime + "|" + password_off
# 创建md5对象
hl = hashlib.md5()
hl.update(s.encode(encoding='utf-8'))
print(s)
print(hl.hexdigest().upper())