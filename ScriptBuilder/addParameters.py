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
        path = os.path.dirname(os.path.abspath('.'))+'/ScriptBuilder'
        self.conf_path = path +'/config.ini'

    def get_config(self):
        conf = ConfigParser()
        conf.read(self.conf_path,encoding = 'UTF-8')
        return conf

    # 比较配置的参数,如果不存在则打印不存在的标签提示
    def compare(self,keys):
        para_list = []
        conf = self.get_config()
        config = conf.items("LOANINFO")
        for i in config:
            para_list.append(str(i[0]))
        invalid = ['loanFeeExtraInfos','lonAttachs','customerInfo','areaList','modelBusinessData', 'propertyMap',
                   'modelId', 'lonContacts', 'tLonAccounts','tLonCreditReport']
        if keys.lower() in para_list and keys not in invalid:
            values = conf.get("LOANINFO", keys)
            return values
        elif keys.lower() not in para_list and keys not in invalid:
            print("配置不存在的标签:%s" % keys)

    def add_parameters(self,centent):
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


if __name__ == '__main__':
    centent ={"productId":"",
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
              "areaList": [{"detailAddr":"","street":"","district":"","city":"","province":"","addrType":""}]}
    addP = addParameters()
    addP.add_parameters(centent)
