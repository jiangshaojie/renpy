# coding=utf-8
import pymysql


class RDS(object):
    def __init__(self, db="partner_settlement"):
        self.db = db

    def __conn(self):
        self.conn = pymysql.connect(host="172.18.2.12",
                                    port=3306,
                                    user="hanxiaobo",
                                    password="123456",
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
