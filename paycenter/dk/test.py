# -*- coding: utf-8 -*-
import hashlib
# s=json.dumps(self.preorderbody)+self.genencrypt()
s='amount=20000&bizNo=1536723280704&notifyUrl=https://www.baidu.com/&operatorId=8706&operatorName=8706&shareInfoBiz=[{"shareService":"renrenche","shareAmount":"1"},{"shareService":"zifang_dg","shareAmount":"2"}]&source=50001&ucid=1032588592796405760&key=r2e0nd9r9fe79nf8e8484ec808264538'
hl = hashlib.md5()
hl.update(s.encode(encoding='utf-8'))
# logger.info("验签字符串"+s)
print(hl.hexdigest())