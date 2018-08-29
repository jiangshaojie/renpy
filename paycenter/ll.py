# -*- coding: utf-8 -*-
import json
a= {'applyPaymentAmount': 1, 'approvalProcess': [], 'bankCode': '104100005619', 'busiLine': '20000', 'busiLineName': '包卖-C1', 'carSourceInformation': '1a1a1aa1a1a1', 'city': '北京', 'collectionAccountBankNo': '6212260200134579313', 'collectionAccountCity': '北京', 'collectionAccountName': '于文胜', 'collectionIDCardNo': '111111111111', 'collectionAccountPhone': '13810148279', 'collectionAccountProvince': '北京', 'collectionBankBranch': '昌平龙泽支行', 'collectionBankName': '中国工商银行', 'exceptPaymentTime': '2018-07-22 10:39:17', 'fundPayNo': 13737080373288, 'paymentType': 2, 'sign': 'AB2322A2EDA36147A6B5CEA8474A8C83', 'createTime': '2018-07-21 10:39:17', 'orderId': '1532140757405'}

print(json.dumps(a))