preorderbody={
      "ucid":"885743499612262400",
      "source":"50002",
      "bizNo":"1535103028935",
      "amount":2,
      "notifyUrl":"https://www.baidu.com/",
      "settleFeeItem":'',
      "shareInfoBiz":"""[{"shareService":"renrenche","shareAmount":"1"},{"shareService":"zifang_dg","shareAmount":"1"}]""",
      "operatorId":8706,
      "operatorName":"8706"
    }

for k,v in preorderbody.items():
    if v=='':
        print(k+'   '+v)