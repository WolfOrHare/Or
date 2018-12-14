#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author  : yangwang
# @Time    : 2018/12/13 11:24
# @Author  : yangwang
# @Email   : 631197757@qq.com
# @File    : addParameters.py
# @Software: PyCharm

from QuerySQL import QuerySQL

class run:
    def __init__(self):
        self.con_db = QuerySQL()
        self.key = []

    # 数据库连接信息
    def db_config(self):
        conlist = self.con_db.connectdb(ssh_host='47.94.40.127',
                                   ssh_usr='appuser',
                                   ssh_psw='5zt4BRJ8',
                                   sql_addr='rdsiuzzzqiuzzzq.mysql.rds.aliyuncs.com',
                                   sql_port=3306,
                                   sql_usr='sit_user01',
                                   sql_psw='j*IHNifVbxCJ',
                                   db_name='test_base_db')
        server = conlist[0]
        con = conlist[1]
        return server,con

    # 根据t_md_prd_cfg_ver表获取产品当前模板id，查询结果为一级属性，如果为单值，该级别下有若干属性使用config_version_id字段与t_md_prd_prop关联，查询所有属性
    # 获取产品模板配置版本,返回版本号
    def get_config_version(self,sql):
        db_config = self.db_config()
        server = db_config[0]
        con = db_config[1]
        result = self.con_db.get_one_values(con, sql)
        server.stop()
        con.close()
        return result


    # 获取当前产品的基础模板配置信息,返回单值\多值的分组列表
    def get_basic_config(self,sql):
        db_config = self.db_config()
        server = db_config[0]
        con = db_config[1]
        result = self.con_db.get_more_value(con, sql)
        server.stop()
        con.close()
        return result

    def get_version(self):
        sql = '''SELECT CONFIG_VERSION_ID FROM t_md_prd_cfg_ver WHERE product_id= 537  and LATEST_VERSION = 'N8701'  and status ='B142002' '''
        res = run.get_config_version(sql)
        return res[0]

    # 返回所有非扩展属性 单属性
    def get_no_extend(self):
        model_cfg_no_extend = '''select m.MODEL_ID,m.`NAME`,p.`NAME` as Keysname,p.DISPLAY_NAME,m.CARDINALITY,m.LINKED_PROPERTY from t_md_prd_model m,t_md_prd_prop p where 
            p.MODEL_ID = m.MODEL_ID 
            and m.EXTEND_MODEL = 'N8702'
            and m.config_version_id = p.CONFIG_VERSION_ID 
            and m.config_version_id =2182 and p.name not in ('uumCustNo','uumUserId') and LINKED_PROPERTY =''  '''
        # 取非扩展表字段
        res = run.get_basic_config(model_cfg_no_extend)
        # 格式化返回信息
        keys = []
        keys_ = []
        format_keys = ''
        for i in res:
            keys.append(i[2])
        for i in range(len(keys)):
            start_ = '"'
            centre_ = '":"",'
            end_ = '":"",'
            if i == 0:
                keys_.append(start_ + keys[i] + centre_)
            elif i == len(keys) - 1:
                keys_.append('"' + keys[i] + end_)
            else:
                keys_.append('"' + keys[i] + centre_)

        return format_keys.join(keys_)

        # 返回所有非扩展属性 属性组
    def get_group_attributeK(self):
        model_cfg_no_extend1 = '''select m.LINKED_PROPERTY,p.`NAME` as Keysname from t_md_prd_model m,t_md_prd_prop p where 
                    p.MODEL_ID = m.MODEL_ID 
                    and m.config_version_id = p.CONFIG_VERSION_ID 
                    and m.config_version_id =2182 and m.LINKED_PROPERTY  <> '' '''

        res = run.get_basic_config(model_cfg_no_extend1)
        # 取扩展表字段
        for i in res:
            if i[0] not in self.key:
                self.key.append(i[0])
            self.key.append(i[1])

        return self.key


    # 返回所有非扩展属性 以字典给形式返回:属性组:标签名-出现次数
    def get_group_attributeN(self):
        m1 = []
        m2 = []
        count = 0
        model_cfg_extend = '''select m.LINKED_PROPERTY,p.`NAME` as Keysname from t_md_prd_model m,t_md_prd_prop p where 
                    p.MODEL_ID = m.MODEL_ID 
                    and m.config_version_id = p.CONFIG_VERSION_ID 
                    and m.config_version_id =2182 and m.LINKED_PROPERTY  <> '' '''
        # 取扩展表字段
        res = run.get_basic_config(model_cfg_extend)
        for i in res:
            if i[0] not in m1:
                m1.append(i[0])

            if i[0] in m1:
                m2.append(i[0])

        result = {}
        for i in set(m1):
            result[i] = m2.count(i)

        return result

    # 返回扩展属性,以字典给形式返回:获取model编号,及出现的次数
    def get_extend_modelN(self):
        m1=[]
        m2=[]
        model_cfg_extend = '''select m.MODEL_ID,p.`NAME` as Keysname,p.DISPLAY_NAME,m.CARDINALITY,m.LINKED_PROPERTY from t_md_prd_model m,t_md_prd_prop p where 
            p.MODEL_ID = m.MODEL_ID 
            and m.config_version_id = p.CONFIG_VERSION_ID 
            and m.EXTEND_MODEL = 'N8701'
            and m.config_version_id =2182 '''
        # 取扩展表字段
        res = run.get_basic_config(model_cfg_extend)
        for i in res:
            if i[0] not in m1:
                m1.append(i[0])

            if i[0]  in m1:
                m2.append(i[0])

        result = {}
        for i in set(m1):
            result[i] = m2.count(i)

        return  result

    # 返回扩展属性,返回所有标签
    def get_extend_modleK(self):
        model_cfg_extend = '''select m.MODEL_ID,p.`NAME` as Keysname,p.DISPLAY_NAME,m.CARDINALITY,m.LINKED_PROPERTY from t_md_prd_model m,t_md_prd_prop p where 
               p.MODEL_ID = m.MODEL_ID 
               and m.config_version_id = p.CONFIG_VERSION_ID 
               and m.EXTEND_MODEL = 'N8701'
               and m.config_version_id =2182 '''
        # 取扩展表字段
        res = run.get_basic_config(model_cfg_extend)
        for i in res:
            if i[0] not in self.key:
                self.key.append(i[0])
            self.key.append(i[1])
        return self.key

    def get_extend_modle26(self):
        x= []
        y = []
        model_cfg_extend = '''select m.MODEL_ID,m.`NAME`,p.`NAME` as Keysname,p.DISPLAY_NAME,m.CARDINALITY,m.LINKED_PROPERTY from t_md_prd_model m,t_md_prd_prop p where 
            p.MODEL_ID = m.MODEL_ID 
            and m.config_version_id = p.CONFIG_VERSION_ID 
            and m.config_version_id =2182 and p.name  in ('uumCustNo','uumUserId') and LINKED_PROPERTY ='' '''
        # 取扩展表字段
        res = run.get_basic_config(model_cfg_extend)
        for i in res:
            x.append(i[0])
            y.append(i[2])
        if 'uumCustNo' in y and 'uumUserId' in y:
            model_26 = ''' {"modelId": "26","propertyMap": {"uumCustNo": "","uumUserId": ""}} '''
            return model_26

        # 扩展属性拼接处理
    def assemble_group(self, modleN, modleV):
        keys_ = []
        format_keys = ''
        for x, y in modleN.items():
            if x in modleV:
                start = '"' + str(x) + '": [{'
                keys_.append(start)
                v = modleV.index(x)
                # modle值的位置+modle出现的次数 == modle包含的key的位置
                vi = v + 1
                vie = vi + y
                count = 0
                # 执行完后删除,用来定位是否结束
                del modleN[x]
                for i in range(vi, vie):
                    count = count + 1
                    k = modleV[i]
                    if count < y:
                        keys_.append('"' + k + '":"",')
                    if count == y and len(modleN) >= 1:
                        keys_.append('"' + k + '":""}],')
                    if count == y and len(modleN) < 1:
                        keys_.append('"' + k + '":""}]')

        return format_keys.join(keys_)

    # 扩展属性拼接处理
    def assemble_model(self, modleN, modleV):
        keys_ = []
        format_keys=''
        for x, y in modleN.items():
            if x in modleV:
                start = '{"modelId":"' + str(x) + '","propertyMap": {'
                keys_.append(start)
                v = modleV.index(x)
                # modle值的位置+modle出现的次数 == modle包含的key的位置
                vi = v + 1
                vie = vi + y
                count = 0
                # 执行完后删除,用来定位是否结束
                del modleN[x]

                for i in range(vi, vie):
                    count = count + 1
                    k = modleV[i]

                    if count < y:
                        keys_.append('"' + k + '":"",')
                    if count == y and len(modleN) >= 1:
                        keys_.append('"' + k + '":""}},')
                    if count == y and len(modleN) < 1:
                        keys_.append('"' + k + '":""}}')

        return format_keys.join(keys_)
    def assembleInfo(self):
        version = self.get_version()
        attribute = self.get_no_extend()
        attributeN = self.get_group_attributeN()
        attributeK = self.get_group_attributeK()

        modelN = self.get_extend_modelN()
        modleK = self.get_extend_modleK()

        model = self.assemble_model(modelN, modleK)
        model26 =  self.get_extend_modle26()
        group = self.assemble_group(attributeN, attributeK)
        print('{' + attribute + group + ',' + '"modelBusinessData": [' + model +','+model26+ ']' + '}')

if __name__ == '__main__':
    # t1 = {38L: 2, 39L: 4, 72L: 1, 77L: 3, 78L: 3, 52L: 2, 86L: 5, 89L: 2, 92L: 4, 93L: 3}
    # t2 = [38L, u'saleLicenceCode', u'orgnCreditCode',
    #       39L, u'communicateAddressDistrict', u'communicateAddressCity', u'communicateAddressProvince', u'customerType',
    #       52L, u'verificationIdentity', u'associationKey', 72L, u'approveEndTime',
    #       77L, u'appId', u'objectId', u'incomeSource', 78L, u'appId', u'objectId', u'hisLoanType',
    #       86L, u'otherLoanPlatformsUnpaid', u'otherLoanPlatformsInfo', u'creditReport', u'currentOverdueAmt',
    #       u'overdueAccNum',
    #       89L, u'businessChannelName', u'businessChannelCode',
    #       92L, u'appId', u'objectId', u'riskType', u'riskValue',
    #       93L, u'arbitrationInst', u'isArbitral', u'arbitralId']
    # for x,y in t1.items():
    #     if x in t2:
    #         bb = t2.index(x)
    #
    #         start = '{"modelId":"' + str(x) + '","propertyMap": {'
    #         print(start)
    #         # 当前的位置+值的位置
    #         count = 0
    #         # 执行完后删除,用来定位是否结束
    #         del t1[x]
    #
    #         for i in range(bb+1,bb + y+1):
    #             count = count + 1
    #             print('--------------------------------',i)
    #             dd = t2[i]
    #
    #             if count < y:
    #                 print('"' + dd + '":"",')
    #             elif count == y and len(t1) >=1:
    #                 print('"' + dd + '":""},')
    #             elif count == y and len(t1) <1:
    #                 print('"' + dd + '":""}')
    # x = run.get_version()
    # x1 = run.get_no_extend()
    # x11 = run.get_group_attributeN()
    # x111 = run.get_group_attributeK()
    #
    # x2 = run.get_extend_modelN()
    # x3 = run.get_extend_modleK()
    #
    # x4 = run.assemble_model(x2, x3)
    # x5 = run.assemble_group(x11,x111)
    #
    # # model_26 = ''' {"modelId": "26","propertyMap": {
    # #  			"uumCustNo": "",
    # # 			"uumUserId": ""
    # # 		}
    # # 	}'''
    # print('{'+x1  +x5 +',' + '"modelBusinessData": ['+ x4 +']'+'}')

    run = run()
    x = run.assembleInfo()
    print(x)
