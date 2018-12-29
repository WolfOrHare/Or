#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Author  : yangwang
# @Time    : 2018/12/13 11:24
# @Author  : yangwang
# @Email   : 631197757@qq.com
# @File    : addParameters.py
# @Software: PyCharm

from configparser import ConfigParser
import os
import json

class addParameters:

    def __init__(self):
        '''
        扩展信息名需要在维护
        '''
        path = os.path.dirname(os.path.abspath('.'))+'/ScriptBuilder'
        self.conf_path = path +'/config.ini'
        self.conf = ConfigParser()
        self.conf.read(self.conf_path, encoding='UTF-8')
        self.invalid = ['loanFeeExtraInfos', 'lonAttachs', 'customerInfo', 'areaList', 'modelBusinessData', 'propertyMap',
               'modelId', 'lonContacts', 'tLonAccounts', 'tLonCreditReport']

    def get_config(self):
        para_list = []
        config = self.conf.items("LOANINFO")
        for i in config:
            para_list.append(i[0])
        return para_list

    # 比较配置的参数,如果不存在则打印不存在的标签提示
    def compare(self,keys):

        invalid = self.invalid
        para_list = self.get_config()

        if keys.lower() in para_list and keys not in invalid:
            values = self.conf.get("LOANINFO", keys)
            return values
        elif keys.lower() not in para_list and keys not in invalid:
            print("配置不存在的标签:%s" % keys)


    def add_parameters_(self,centent):
        json_data = json.load(centent)
        invalid = ['loanFeeExtraInfos','lonAttachs','customerInfo','areaList','modelBusinessData', 'propertyMap',
                   'modelId', 'lonContacts', 'tLonAccounts','tLonCreditReport']
        compare = self.compare
        print(centent)
        # 传入参数应为字典
        if isinstance(centent,dict):
            # 拆解后,如果是字典继续拆解后直接赋值给对应的字典,是list读取到list的值后判断是否是字典
            for k, v in centent.items():
                if isinstance(v,dict):
                    for k1,v1 in v.items():
                        if k1 not in invalid:
                            centent[k1] = compare(k1)
                            print("111111111k1: %s:不是list标签" % k1)
                        else:
                            print("111111111k1: %s:为list标签" % k1)
                elif isinstance(v,list):
                    for k1,v1 in v[0].items():
                        if isinstance(v1, list):
                            for k11, v11 in v1[0].items():
                                if k11 not in invalid:
                                    centent[k11] = compare(k11)
                                    print("k11: %s:不是list标签" % k11)
                                else:
                                    print("k11: %s:为list标签" % k11)

                        elif isinstance(v1, dict):
                            for k11, v11 in v1.items():
                                if k11 not in invalid:
                                    centent[k11] = compare(k11)
                                    print("k11: %s:不是list标签" % k11)
                                else:
                                    print("k11: %s:为list标签" % k11)

                        else:
                            if k1 not in invalid:
                                centent[k1] = compare(k1)
                                print("222222222k1: %s:不是list标签" % k1)
                            else:
                                print("222222222k1: %s:为list标签" % k1)
                else:
                    if k not in invalid:
                        centent[k] = compare(k)
                        print("k: %s:不是list标签" % k)
                    else:
                        print("k: %s:为list标签" % k)

            print(centent)
            return  centent


    def add_parameters(self, centent):
        date_json = json.loads(centent)
        # date_json = json.loads(SendRegisterVerificationCodejson_txt)
        print(date_json)
        print("*" * 100)
        # 遍历json文件所有的key对应的value
        dic = {}
        def json_txt(dic_json):
            if isinstance(dic_json, dict):  # 判断是否是字典类型isinstance 返回True false
                for key in dic_json:
                    if isinstance(dic_json[key], dict):  # 如果dic_json[key]依旧是字典类型
                        print("****key1--：%s value--: %s" % (key, dic_json[key]))
                        json_txt(dic_json[key])
                        dic[key] = dic_json[key]
                    elif isinstance(dic_json[key], list): # 如果是list，获取所有内容
                        for dic_ in dic_json[key]:
                            print("****key2--：%s value--: %s" % (key, dic_))
                            json_txt(dic_)
                            # dic[key] = dic_
                    else:
                        print("****key3--：%s value--: %s" % (key, dic_json[key]))
                        dic[key] = dic_json[key]

        json_txt(date_json)
        print("dic ---: " + str(dic))

        def check_json_value(dic_json,k,v):
            if isinstance(dic_json,dict):
                for key in dic_json:
                    if key == k:
                        dic_json[key] = v
                    elif isinstance(dic_json[key],dict):
                        check_json_value(dic_json[key],k,v)
                    elif isinstance(dic_json[key],list):
                        for dic_ in dic_json[key]:
                            check_json_value(dic_, k, v)


        print("date_json 变更前   :")
        print(date_json)
        for i in dic:
            if i not in self.invalid:
                v = self.compare(i)
                check_json_value(date_json,i,v)
        print("date_json 变更后   :")
        print(json.dumps(date_json))

if __name__ == '__main__':
    centent ='''{"productId":"",
              "modelBusinessData": [{"modelId":"38","propertyMap": {"saleLicenceCode":"","orgnCreditCode":""}},
                                    {"modelId":"39","propertyMap":
                                        {"communicateAddressDistrict":"", "communicateAddressCity":"",
                                    "communicateAddressProvince":"","customerType":""}},
                                    {"modelId":"72","propertyMap": {"approveEndTime":""}},
                                    {"modelId":"77","propertyMap": {"appId":"","objectId":"","incomeSource":""}},
                                    {"modelId":"78","propertyMap": {"appId":"","objectId":"","hisLoanType":""}},
                                    {"modelId":"52","propertyMap": {"verificationIdentity":"","associationKey":""}},
                                    {"modelId":"86","propertyMap": {"otherLoanPlatformsUnpaid":"",
                                "otherLoanPlatformsInfo":"","creditReport":"","currentOverdueAmt":"","overdueAccNum":""}},
                                    {"modelId":"89","propertyMap": {"businessChannelName":"","businessChannelCode":""}},
                                    {"modelId":"92","propertyMap": {"appId":"","objectId":"","riskType":"","riskValue":""}},
                                    {"modelId":"93","propertyMap": {"arbitrationInst":"","isArbitral":"","arbitralId":""}},
                                    {"modelId": "26","propertyMap": {"uumCustNo": "","uumUserId": ""}} ],"saleChannel":"","instCode":"","customerName":"",
              "phone":"","certId":"","marry":"","degree":"",
              "eMail":"","liveAddress":"",
              "certType":"","company":"","intustry":"","career":"","loanPurpose":"",
    "borrowerType":"","approveAmt":"","approveLimit":"","appayDate":"","oldAppId":"","customerInfo":
                  [{"hasLoan":"","incomeSource":"","monthlyIncome":"","hisLoanType":""}],
              "lonContacts": [{"contactRelation":"","contactName":"","contactPhone":""}],
              "lonAttachs": [{"attachType":"","attachName":"","fileId":"","fileType":""}],
              "tLonAccounts": [{"accAccountName":"","accAccount":"","trusteeType":"","accType":"","accountType":"",
                                "accOwnIdCard":"","accCertType":"","accOwnPhone":"","accCorpRep":"","accOwnName":"",
                                "accBankCard":"","accCity":"","accProvince":"","accBankBranch":"","accBankName":"",
                                "accBankCardBindId":"","uumCustNo":"","extendFieldString":"","accSubAccountNo":""}],
              "tLonCreditReport": [{"score":"","riskGrade":""}], "loanFeeExtraInfos": [{"infoValue":"","infoName":""}],
              "areaList": [{"detailAddr":"","street":"","district":"","city":"","province":"","addrType":""}]} '''
    addP = addParameters()
    addP.add_parameters(centent)
