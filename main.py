#coding=utf-8

import sys

print(sys.getdefaultencoding())



str1 = '\xe5\x9b\xbd\xe5\x8a\xa1\xe9\x99\xa2\xe6\x89\xb9\xe5\xa4\x8d\xe5\x90\x8c\xe6\x84\x8f\xe3\x80\x8a\xe5\x8c\x97\xe4\xba\xac\xe5\x9f\x8e\xe5\xb8\x82\xe5\x89\xaf\xe4\xb8\xad\xe5\xbf\x83\xe5\xbb\xba\xe8\xae\xbe\xe5\x9b\xbd\xe5\xae\xb6\xe7\xbb\xbf\xe8\x89\xb2\xe5\x8f\x91\xe5\xb1\x95\xe7\xa4\xba\xe8\x8c\x83\xe5\x8c\xba\xe5\xae\x9e\xe6\x96\xbd\xe6\x96\xb9\xe6\xa1\x88\xe3\x80\x8b'

print(str1.encode('latin-1').decode('utf-8'))

govs = [
        "https://www.gov.cn/zhengce/zuixin",
        "https://www.gov.cn/zhengce/wenjian/zhongyang"
    ]
mems = [
    "http://mem.gov.cn/gk/tzgg/bl",
    "http://mem.gov.cn/gk/tzgg/tb",
    "http://mem.gov.cn/gk/tzgg/yjbgg",
    "http://mem.gov.cn/gk/tzgg/tz",
    "http://mem.gov.cn/gk/tzgg/h",
    "http://mem.gov.cn/gk/tzgg/yj",
    "http://mem.gov.cn/gk/tzgg/qt",
]

start_urls = govs + mems
print(start_urls)
import pymysql

# 连接 MySQL 数据库
conn = pymysql.connect(
    host='127.0.0.1',  # 主机名
    port=3306,  # 端口号，MySQL默认为3306
    user='root',  # 用户名
    password='baifachuan',  # 密码
    database='policy_db',  # 数据库名称
)

# 创建游标对象
cursor = conn.cursor()
# 执行 SQL 查询语句
cursor.execute("SELECT * FROM policy")
# 获取查询结果
result = cursor.fetchall()

print("./202403/t20240318_1948497.html"[2: len("./202403/t20240318_1948497.html")])
