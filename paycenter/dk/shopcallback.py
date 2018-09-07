#encoding:utf-8
import hashlib
class shopcallback():
    fyurl="http://127.0.0.1:8380/v1/notify/fy"
    def fycallback(self,amt='20000',bankcard='6214830102054581',MCHNTORDERID='20180905105518802000001E0ZQGN21F',responsecode='0000',responsemsg='成功'):
        # mchntCd='0002900F0096235'
        secretKey='5old71wihg2tqjug9kkpxnhx9hiujoqj'
        data={'TYPE': '03', 'VERSION': '1.0', 'MCHNTCD': '0002900F0096235', 'USERID': '1236985478',
              'RESPONSECODE': '0000', 'RESPONSEMSG': '成功', 'MCHNTORDERID': '14909408631788350725',
              'ORDERID': '000037040038', 'AMT': '200', 'BANKCARD': '6226090217436936',
              'PROTOCOLNO': '14907763938986631631'}
        data["AMT"]=amt
        #amt 金额，bankcard 银行卡号,MCHNTORDERID 商户订单号
        # data['MCHNTCD']=mchntcd
        data['RESPONSECODE']=responsecode
        data['RESPONSEMSG']=responsemsg
        data['BANKCARD']=bankcard
        data['MCHNTORDERID']=MCHNTORDERID

        signstring=data["TYPE"]+"|"+data["VERSION"]+"|"+data["RESPONSECODE"]+"|"+data["MCHNTCD"]+"|"+data["MCHNTORDERID"]+"|"+data["ORDERID"]+"|"+data["AMT"]+"|"+data["BANKCARD"]+"|"+secretKey
        sign=hashlib.md5()
        sign.update(signstring.encode(encoding='utf-8'))
        print(sign.hexdigest())

    def fycallbacks(self):
        data="{RESPONSECODE=0000, AMT=10000, BANKCARD=6214830102054581, ORDERID=000036667311, REM1=, SIGNTP=md5, PROTOCOLNO=C7Q8SJ100000017087OR5E, RESPONSEMSG=成功, MCHNTCD=0002900F0096235, MCHNTORDERID=201808281437125600000063HR7816JJ, VERSION=1.0, USERID=20180828103052279000007251442874, SIGN=5d14b4712f839f75de4a0fc5b9134878, TYPE=03, REM2=, REM3=}"

if __name__=='__main__':
    a=shopcallback()
    a.fycallback()
