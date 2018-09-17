#encoding:utf-8
from log import logger
from  utils.RDSWrapper import RDS
def localdkfoursign():
    #统计本地四要素数量，并打印出差异
    filepath='C:/Users/jiangshaojie/Desktop/线上.txt'
    cards=set()
    # bank_type=list()
    bank_type=["0025840","0403","PSBC", "1021000", "0102", "ICBC","1031000", "0103", "ABC","1041000", "0104", "BOC","1051000", "0105", "CCB","3011000", "0301", "BCOM","3021000", "0302", "CITIC","3031000", "0303", "CEB","3041000", "0304", "HXB","3051000", "0305", "CMBC","3065810", "0306", "GDB","3135840", "0307", "PAB","3085840", "0308", "CMB","3091000", "0309", "CIB","3102900", "0310", "SPDB"]
    with open(filepath,'r',encoding='utf-8') as fileobject:
        lines=fileobject.readlines()
        for item in lines:
            entry=item.split(',')[3]
            if entry in bank_type:
                # logger.info("符合要求"+item)
                # print("符合要求"+item)
                entry=item.split(',')[0]+item.split(',')[4]
                cards.add(entry)
            else:
                logger.info("不符合要求"+item)
        datarcord=get_ids()

        for i in cards:
            if i not in datarcord:
                print(i)
        print(cards.__len__())
        print(len(cards))
def localdksign():
    #统计本地dk_sign 签约数量
    filepath='C:/Users/jiangshaojie/Desktop/线上.txt'
    cards=set()
    # bank_type=list()
    bank_type=["0025840","0403","PSBC", "1021000", "0102", "ICBC","1031000", "0103", "ABC","1041000", "0104", "BOC","1051000", "0105", "CCB","3011000", "0301", "BCOM","3021000", "0302", "CITIC","3031000", "0303", "CEB","3041000", "0304", "HXB","3051000", "0305", "CMBC","3065810", "0306", "GDB","3135840", "0307", "PAB","3085840", "0308", "CMB","3091000", "0309", "CIB","3102900", "0310", "SPDB"]
    with open(filepath,'r',encoding='utf-8') as fileobject:
        lines=fileobject.readlines()

        types=[7,8]


        # print(types(lines[0].split(',')[7]))
        for item in lines:
            entry=item.split(',')[7]
            # print(entry)
            for i in types:
                if i == int(entry):
                    cards.add(item.split(',')[0] + item.split(',')[4]+item.split(',')[7])


        print(cards.__len__())
        print(len(cards))
def get_ids(orderid=""):
    datarecord=list()
    rds = RDS(db="rrcp_account")
    sql = "SELECT ucid,card_no FROM dk_four_sign "
    logger.info('查询approval_id sql： '+sql.__str__())
    approval_id = rds.select(sql)
    for item in approval_id:
        datarecord.append(item['ucid']+item['card_no'])
    return datarecord
def localusrmauth():
    filepath = 'C:/Users/jiangshaojie/Desktop/线上.txt'
    cards = set()
    # bank_type=list()
    with open(filepath, 'r', encoding='utf-8') as fileobject:
        lines = fileobject.readlines()
        for item in lines:
            ucid=item.strip().split(',')[0]
            if int(ucid) >0:

                cards.add(ucid)
    print(len(cards))

if __name__=='__main__':
    # get_ids()
    # localrecord()
    # localdkfoursign()
    # localdksign()
    localusrmauth()