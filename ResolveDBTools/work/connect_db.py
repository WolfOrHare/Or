# -*- coding: utf-8 -*-
'''
Created on 2018.01.24
@author: wuyou
'''

import MySQLdb
from sshtunnel import SSHTunnelForwarder
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class QuerySQL():

    def connectssh(self, dbinfo):
        server = SSHTunnelForwarder(
            (dbinfo['ssh_host'], 22),
            ssh_username=dbinfo['ssh_usr'],
            ssh_password=dbinfo['ssh_psw'],
            remote_bind_address=(dbinfo['sql_addr'],
                                 int(dbinfo['sql_port'])))
        server.start()
        return server

    def stopserver(self, server, con):
        server.stop()
        con.close()

    def stopssh(self, server):
        server.stop()

    # 连接数据库方法
    def connectdb(self, ssh_host, ssh_usr, ssh_psw, sql_addr, sql_port, sql_usr, sql_psw, db_name):
        server = SSHTunnelForwarder(
            (ssh_host, 22),
            ssh_username=ssh_usr,
            ssh_password=ssh_psw,
            remote_bind_address=(sql_addr, int(sql_port)))
        server.start()
        serverport = server.local_bind_port
        con = MySQLdb.connect(host='127.0.0.1',
                              #							   port=server.local_bind_port,
                              port=serverport,
                              user=sql_usr,
                              passwd=sql_psw,
                              db=db_name,
                              charset='utf8')
        return server, con, serverport

    # 基础平台数据库连接
    def connect_basedb(self, dbinfo):
        ssh_host = dbinfo['bs_ssh_host']
        ssh_usr = dbinfo['bs_ssh_usr']
        ssh_psw = dbinfo['bs_ssh_psw']
        sql_addr = dbinfo['base_addr']
        sql_port = dbinfo['base_port']
        sql_usr = dbinfo['base_usr']
        sql_psw = dbinfo['base_psw']
        db_name = dbinfo['base_db']
        # print u'%s，%s，%s，%s，%s，%s，%s，%s'%(ssh_host,ssh_usr,ssh_psw,sql_addr,sql_port,sql_usr,sql_psw,db_name)
        (server, con, serverport) = self.connectdb(ssh_host, ssh_usr, ssh_psw, sql_addr, sql_port, sql_usr, sql_psw,
                                                   db_name)
        return server, con, serverport

    # 贷款数据库连接
    def connect_loandb(self, dbinfo):
        ssh_host = dbinfo['ssh_host']
        ssh_usr = dbinfo['ssh_usr']
        ssh_psw = dbinfo['ssh_psw']
        sql_addr = dbinfo['sql_addr']
        sql_port = dbinfo['sql_port']
        sql_usr = dbinfo['sql_usr']
        sql_psw = dbinfo['sql_psw']
        db_name = dbinfo['sql_db']
        (server, con, serverport) = self.connectdb(ssh_host, ssh_usr, ssh_psw, sql_addr, sql_port, sql_usr, sql_psw,
                                                   db_name)
        return server, con, serverport

    # 查询所有表名

    #
    def get_table_name(self, db, sql,_header):
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        resultlist = []
        dict1 = []
        for i in range(len(result)):
            resultlist.append(result[i])
            for i in resultlist[i]:

                if _header in i:
                    dict1.append(i)

        return dict1

    # 用于解析查询到的建表脚本
    def show_create_table(self,db,tablename):

        sql = '''show create table %s''' % tablename
        cursor = db.cursor()
        try:
            cursor.execute(sql)
        except:
            print('show create table Fail!!!')
        result = cursor.fetchall()

        if result == ():
            result = '0'
        else:
            result = result[0][1]
            #print(result)
        return result

    # 单字段记录查询
    def get_one_value(self, db, sql):
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()

        if result == ():
            result = '0'
        else:
            result = result[0][0]
        return result
    # 单条记录查询
    def get_one_values(self, db, sql):
        cursor = db.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        if result == ():
            result = '无记录'
        else:
            result = result[0]
        return result

    # 多条记录查询
    def get_more_value(self, db, sql):
        cursor = db.cursor()
        test_sql = str(sql)
        cursor.execute(test_sql)
        data = cursor.fetchall()
        return data

    # 数据更新-update
    def update_value(self, db, sqlcommand):
        update_result = 'update success：' + sqlcommand
        cursor = db.cursor()
        try:
            cursor.execute(sqlcommand)
            db.commit()
        except:
            update_result = 'update fail：' + sqlcommand
        print(update_result)

    # 根据风险等级，到数据库查平台的风险备用金率
    def get_serviceRate(self, data, dbinfo):

        riskGrade = data['riskGrade']
        productId = data['productId']
        term = data['loanTerm']
        (server, con, port) = self.connect_basedb(dbinfo)
        if riskGrade == "AA":
            riskGrade = "A_A"
        if riskGrade == "BB":
            riskGrade = "B_B"
        sql = "SELECT CONVERT(LEVEL_" + riskGrade + ",CHAR) FROM t_prd_consult_service_rate WHERE \
	       PRODUCT_ID='" + productId + "' AND times='" + term + "' ORDER BY create_time DESC LIMIT 1"
        serviceRate = self.get_one_value(con, sql)
        server.stop()
        con.close()
        return serviceRate

    def get_riskFundRate(self, data, dbinfo):
        riskGrade = data['riskGrade']
        productId = data['productId']
        term = data['loanTerm']
        (server, con, port) = self.connect_basedb(dbinfo)
        if riskGrade == "AA":
            riskGrade = "A_A"
        if riskGrade == "BB":
            riskGrade = "B_B"
        sql = "SELECT CONVERT(LEVEL_" + riskGrade + ",CHAR) FROM t_prd_risk_fund WHERE \
	       PRODUCT_ID='" + productId + "' AND times='" + term + "' ORDER BY create_time DESC LIMIT 1"
        # print sql
        riskFundRate = self.get_one_value(con, sql)
        server.stop()
        con.close()
        return riskFundRate

    def Query_application(self, APPID, Envir, con):
        # 该函数用于查询工单表相关信息
        sql = "SELECT APPROVE_AMT,APPROVE_LIMIT,YEAR_RATE,MONTH_RATE,LOAN_DATE,\
	    PRODUCT_ID,PRODUCT_VERSION,CONTRACT_AMT,MONTH_REPAY_LIMIT,DRAWN_AMT,REPAY_DAY FROM " \
              + Envir['sql_db'] + ".t_lon_application WHERE APP_ID='" + str(APPID) + "'"

        db_query = self.get_one_values(con, sql)
        application = {}
        application['APPROVE_AMT'] = db_query[0]
        application['APPROVE_LIMIT'] = db_query[1]
        application['YEAR_RATE'] = db_query[2]
        application['MONTH_RATE'] = db_query[3]
        application['LOAN_DATE'] = db_query[4][0:10]
        application['PRODUCT_ID'] = db_query[5]
        application['PRODUCT_VERSION'] = db_query[6]
        application['CONTRACT_AMT'] = db_query[7]
        application['MONTH_REPAY_LIMIT'] = db_query[8]
        application['DRAWN_AMT'] = db_query[9]
        application['REPAY_DAY'] = db_query[10]

        return application

    def Query_Risk_Grade(self, APPID, Envir, con):
        # 该函数用于查询风险等级

        sql = "SELECT RISK_GRADE FROM " + Envir['sql_db'] + \
              ".t_lon_credit_report WHERE APP_ID='" + str(APPID) + "' and CREDIT_TYPE='F0210'"

        db_query = self.get_one_value(con, sql)

        application = {}
        application['RISK_GRADE'] = db_query[0]

        return application

    def Query_Comm(self, table, PRODUCT_ID, VERSION, TIMES, Risk_Grade, Envir, con):
        # 该函数主要是基础平台相关费率
        # 信用管理费费率
        # 恒元费用比例
        # 保险费费率
        # 咨询服务费率
        # 贷后管理费费率
        # 担保费率（比例）
        sql = "SELECT LEVEL_A,LEVEL_B,LEVEL_C,LEVEL_D,LEVEL_E,LEVEL_A_A,LEVEL_B_B FROM " \
              + str(table) + " WHERE PRODUCT_ID='" + str(PRODUCT_ID) + "' AND VERSION='" + str(VERSION) + \
              "' AND TIMES='" + str(TIMES) + "'"
        db_query = self.get_one_values(con, sql)

        list_risk_grade = ['A', 'B', 'C', 'D', 'E', 'AA', 'BB']
        for i in range(7):
            if list_risk_grade[i] == Risk_Grade:
                break
        if db_query == None:
            value = 0
        else:
            value = db_query[i]

        return value

    def Query_Fee_Amt(self, APPID, FEE_TYPE, Envir, con):
        # 查询费用表
        sql = "SELECT FEE_AMT FROM " + Envir['sql_db'] + ".t_loan_fee_info WHERE APP_ID='" + str(APPID) + \
              "' AND FEE_TYPE='" + FEE_TYPE + "'"
        db_query = self.get_one_values(con, sql)
        if db_query == None:
            value = 0
        else:
            value = db_query[0]

        return value

    def Query_fee_extra_info(self, APPID, INFO_NAME, Envir, con):
        # 查询扩展费用表——表数据来源为进件成功后插入到该表
        sql = "SELECT INFO_VALUE FROM " + Envir['sql_db'] + ".pl_loan_fee_extra_info WHERE APP_ID='" + str(APPID) + \
              "' AND INFO_NAME='" + INFO_NAME + "'"
        db_query = self.get_one_value(con, sql)
        if db_query == None and INFO_NAME == 'B6640':
            value = 0
        elif db_query == None and INFO_NAME != 'B6640':
            value = INFO_NAME + "在拓展费用表无记录，请核对入参是否正确"
        else:
            value = db_query[0]
        return value

    def Query_prop_value_info(self, APPID, PROPERTY_NAME, Envir, con):
        # 查询扩展属性值表——表数据来源为进件成功后插入到该表
        sql = "SELECT STRING_VALUE FROM " + Envir['sql_db'] + ".t_lon_prop_value WHERE APP_ID='" + str(APPID) + \
              "' AND PROPERTY_NAME='" + PROPERTY_NAME + "'"
        db_query = self.get_one_value(con, sql)
        if db_query == None:
            value = 0
            print ("t_lon_prop_value表中未查询到" + PROPERTY_NAME + "的记录")
        else:
            value = db_query[0]
        return value

    def Query_Repayment_Plan(self, APPID, value, Envir, con):
        # 查询还款计划表信息
        # parameter定义了从还款计划表中查询的字段，parameter之外的将在费用计划表查询
        parameter = ['STAGE', 'PLAN_REPAY_DATE', 'PLAN_REPAY_AMT', 'REMAIN_PRINCIPAL_AMT', 'INTEREST', 'PRINCIPAL',
                     'REPAY_OFF_AMT']
        # 拼接SQL
        sql = "SELECT "
        # 遍历：如果不在parameter内，添加子查询语句；否则，正常拼接字段名
        for p in range(len(value)):
            if value[p] not in parameter:
                sql = sql + "ifnull((SELECT PLAN_REPAY_AMT FROM t_rep_repayment_fees WHERE APP_ID=t.app_id and STAGE=t.STAGE and PLAN_REPAY_DATE = t.PLAN_REPAY_DATE and FEE_CODE='" + \
                      value[p] + "'),0) as '" + str(value[p]) + "',"
            else:
                sql = sql + str(value[p]) + ","
        # 去掉最后一个字符，
        sql = sql[:-1]
        sql = sql + " FROM " + Envir['sql_db'] + ".t_rep_repayment t WHERE APP_ID='" + str(APPID) + "'"
        db_query = self.get_more_value(con, sql)
        return db_query


if __name__ == '__main__':
    run = QuerySQL()

    sqlcommand = '''select table_name from information_schema.tables where table_schema='test_loan_db' and table_type='base table' '''
    # conlist = run.connectdb(dbinfo)

    conlist = run.connectdb(ssh_host='47.94.40.127', ssh_usr='appuser', ssh_psw='5zt4BRJ8',
                            sql_addr='rdsiuzzzqiuzzzq.mysql.rds.aliyuncs.com', sql_port=3306,
                            sql_usr='sit_user01', sql_psw='j*IHNifVbxCJ', db_name='test_base_db')

    server = conlist[0]
    con = conlist[1]
    result = run.get_one_value(con, sqlcommand)
    server.stop()
    con.close()
    # print result

##
# #SSH配置信息
#     ${ssh_host}    set variable    47.94.40.127
#     ${ssh_name}    set variable    appuser
#     ${ssh_psw}    set variable    5zt4BRJ8
#     ${rds_addr}    set variable    rdsiuzzzqiuzzzq.mysql.rds.aliyuncs.com
##