# coding=utf-8
import pymysql


class RDS(object):
    def __init__(self, db="partner_settlement"):
        self.db = db

    def __conn(self):
        self.conn = pymysql.connect(host="rdsqv39909q66i6efi0k.mysql.rds.aliyuncs.com",
                                    port=3306,
                                    user="work",
                                    password="RqQb5YFfOH5ojZ16",
                                    db=self.db,
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)

    def select(self, query):
        try:
            self.__conn()
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        finally:
            self.conn.close()

    def commit_sql(self, query):
        try:
            self.__conn()
            with self.conn.cursor() as cursor:
                cursor.execute(query)
                self.conn.commit()
                return 0
        finally:
            self.conn.close()
