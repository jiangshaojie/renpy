# -*- coding: utf-8 -*-
import mysql.connector
def connectdb():
    db=mysql.connector.connection(user='root', password='password', database='test', use_unicode=True)
    return db
def querydb():
    db=connectdb()
    cursor=db.cursor()
