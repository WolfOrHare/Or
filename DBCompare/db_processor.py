# -*- coding: utf-8 -*-
import os
from function.QuerySQL import QuerySQL
import settings


class db_processor(object):
    def __init__(self):
        self.config_tb = settings.setting.TABLELIST
        self.config_sql = settings.setting.SQL

    def getSQLList(self):
        sql = ''
        # if sqlcommand in
        if self.config_tb in self.config_sql:
            sql = self.config_sql['config_tb']
        elif len(self.config_sql) != len(self.config_tb):
            print(self.config_tb)
            print(self.config_sql)
            print("warning...conf lenth !=")
        else:
            print("没有相应配置文件")
        return sql

    def select_table(self,sql):
        con_db = QuerySQL()
       # conlist = run.connectdb(dbinfo)

        conlist = con_db.connectdb(ssh_host='47.94.40.127',
                                   ssh_usr='appuser', ssh_psw='5zt4BRJ8',
                                   sql_addr='rdsiuzzzqiuzzzq.mysql.rds.aliyuncs.com',
                                   sql_port=3306,
                                   sql_usr='sit_user01',
                                   sql_psw='j*IHNifVbxCJ',
                                   db_name='test_base_db')
        server = conlist[0]
        con = conlist[1]

        result = con_db.get_one_values(con,sql)
        # print(result)
        server.stop()
        con.close()

        return result
#
# sql = '''select LEVEL_A_A,LEVEL_A,LEVEL_B_B,LEVEL_C,LEVEL_D,LEVEL_E,LEVEL_O from t_prd_consult_service_rate where PRODUCT_ID = 298 and times = %s'''
# x = select_table(sql%6)
