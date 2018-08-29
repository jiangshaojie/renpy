# -*- coding: utf-8 -*-
from log import logger
import  requests,json
class createshop(object):
    header = """
       User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36
       Accept: application/json, text/plain, */*
       Accept-Encoding: gzip, deflate
       Accept-Language: zh-cn
       Content-Type: application/json
       """
    data = {"shopName": "创建测试01", "shopShortName": "创建测试01", "serviceType": "检测,维修", "serviceCity": "北京",
            "address": "dfsf", "gdLongitude": "111", "gdLatitude": "111", "bdLongitude": "111", "bdLatitude": "111",
            "contact": "12312312", "phone": "13566896536", "status": "NORMAL", "businessId": "FWS-BJ-00010140",
            "businessName": "服务商测试01", "province": "福建省", "city": "福州", "area": "鼓楼"}
    cookie = 'sellet=s%3AMIcdjdl06AHkpknQC9mFYc6Ty7Vu5FAJ.oK7BIsoefWBFseleOAuuqSBA06H0BxGjNRRg5tPUO9I'

    def headers_to_dict_default(self):
        # 将字符串转换成字典
        headers = self.header.split('\n')
        header = dict()
        for i in headers:
            h = i.strip()
            if h:
                k, v = h.split(":", 1)
                header[k] = v.strip()
        header['Cookie']=self.cookie
        return header


    def getplace(self,place):
        """
        :param place:
        :return: list : [福建省,福州,鼓楼]
        """
        with open(file='D:/renpy/paycenter/allcities.txt',encoding='utf-8') as file:
            cityies=json.load(file)['data']
            re=list()
            for item in cityies:
                item_child=item['children']
                for i in item_child:
                    if i['value']==place:
                        re.append(item['value'])
                        re.append(i['value'])
                        re.append(i['children'][0]['value'])
                        # re=item['value']+' '+i['value']+' '+i['children'][0]['value']
                        # print(re)
                        logger.info("省市区："+re.__str__())
                        return re


    def getgps(self,place):
        """

        :param place:
        :return: list 第一项为latitude,第二项为 longitude
        """
        re=list()
        city=place[1]
        county=place[2]
        with open(file='D:/renpy/paycenter/gpss.txt', encoding='utf-8') as file:
            gps=set()
            for i in file.readlines():
                gps.add(i.strip())

            for  i in gps:
                if len(i)<1:
                    gps.remove(i)
                    break
            # print(gps)
            for i in gps:
                item=json.loads(i)
                if city==item['city'][0:len(city)] and county==item['county'][0:len(county)]:
                    re.append(item['latitude'])
                    re.append(item['longitude'])
                    break
            logger.info("获得的经纬度："+re.__str__())
            return re


    def createpost(self,data):
        rurl='http://10.44.138.237:8384/api/shop/service_point_create'
        reheader=self.headers_to_dict_default()
        logger.info("创建服务商请求header:"+reheader.__str__())
        logger.info("创建服务商json数据："+json.dumps(self.data))
        res=requests.post(url=rurl,data=json.dumps(data),headers=reheader)

        logger.info("创建服务商返回结果"+res.__str__())
        logger.info("创建服务商返回结果内容"+res.text)


    def getopencity(self):
        rurl = 'http://10.44.138.237:8384/api/open_cities'
        reheader = self.headers_to_dict_default()
        logger.info("获取开站城市请求header："+reheader.__str__())
        res = requests.get(url=rurl,headers=reheader)
        if res.status_code==200:
            logger.info("开站城市列表"+res.text)
            return json.loads(res.text)['data']


    def createshop(self,cityies,businessid,businessname):
        """

        :param cityies: '北京,上海' 以',' 分割的城市列表
        :return:
        """
        # self.data['businessId']=businessid
        # self.data['businessName'] = businessname
        datas=self.data
        datas['businessId'] = businessid
        datas['businessName'] = businessname
        createcityies=cityies.split(',')
        opencities=self.getopencity()
        for city in createcityies:
            if opencities.__contains__(city):
                place=self.getplace(city)
                gps=self.getgps(place)
                datas['shopName']='包卖联调'+city
                datas['shopShortName']='包卖联调'+city
                datas['serviceCity']=city
                datas['address']='包卖联调'+city
                datas['contact']='包卖联调'+city
                datas['gdLongitude'] = gps[0]
                datas['gdLatitude'] = gps[1]
                datas['bdLongitude'] = gps[0]
                datas['bdLatitude'] = gps[1]
                # datas['gdLongitude']=gps[1]
                # datas['gdLatitude']=gps[0]
                # datas['bdLongitude']=gps[1]
                # datas['bdLatitude']=gps[0]
                datas['province']=place[0]
                datas['city']=place[1]
                datas['area']=place[2]
                self.createpost(datas)
            else:
                logger.info(city+' ,未在开站城市列表内')
                place = self.getplace('北京')
                gps = self.getgps(place)
                datas['shopName'] = '包卖联调' + city
                datas['shopShortName'] = '包卖联调' + city
                datas['serviceCity'] = city
                datas['address'] = '包卖联调' + city
                datas['contact'] = '包卖联调' + city
                datas['gdLongitude'] = gps[0]
                datas['gdLatitude'] = gps[1]
                datas['bdLongitude'] = gps[0]
                datas['bdLatitude'] = gps[1]
                # datas['gdLongitude'] = gps[1]
                # datas['gdLatitude'] = gps[0]
                # datas['bdLongitude'] = gps[1]
                # datas['bdLatitude'] = gps[0]
                datas['province'] = place[0]
                datas['city'] = place[1]
                datas['area'] = place[2]
                self.createpost(datas)

def test(self):
    requests.utils.cookiejar_from_dict()
    pass







if __name__=='__main__':
    cityies='洛阳'
    businessid="FWS-BJ-00010082"
    businessname="服务点统一签署的服务商"

    # businessid = "FWS-BJ-00010140"
    # businessname = "服务商测试01"
    a=createshop()
    # # a.createpost()
    # re=a.getopencity()
    # print(type(re),re)
    a.createshop(cityies,businessid,businessname)
    # a.getopencity()


