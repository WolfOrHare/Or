# -*- coding: utf-8 -*-
# from QuerySQL import QuerySQL
import json
sql = '''SELECT * FROM t_md_prd_model  WHERE config_version_id =2182 '''
class test:
    def __init__(self):
        # self.con_db = QuerySQL()

        self.conlist = []

    # def check(self,func):
    #
    #     def inner():
    #         self.con_db.connectdb(ssh_host='47.94.40.127',
    #                                    ssh_usr='appuser', ssh_psw='5zt4BRJ8',
    #                                    sql_addr='rdsiuzzzqiuzzzq.mysql.rds.aliyuncs.com',
    #                                    sql_port=3306,
    #                                    sql_usr='sit_user01',
    #                                    sql_psw='j*IHNifVbxCJ',
    #                                    db_name='test_base_db')
    #         return func()
    #
    #     return inner
    #
    #
    # @check
    # def get_config_version(self):
    #
    #     server = self.conlist[0]
    #     con = self.conlist[1]
    #     result = self.con_db.get_one_values(con, sql)
    #     print(result)
    #     server.stop()
    #     con.close()
    #     return 0

    def add_parameters(self):
        centent = """{"productId": "",
               "modelBusinessData": [{"modelId": "38", "propertyMap": {"saleLicenceCode": "", "orgnCreditCode": ""}},
                                     {"modelId": "39", "propertyMap":
                                         {"communicateAddressDistrict": "", "communicateAddressCity": "",
                                          "communicateAddressProvince": "", "customerType": ""}},
                                     {"modelId": "72", "propertyMap": {"approveEndTime": ""}},
                                     {"modelId": "77",
                                      "propertyMap": {"appId": "", "objectId": "", "incomeSource": ""}},
                                     {"modelId": "78", "propertyMap": {"appId": "", "objectId": "", "hisLoanType": ""}},
                                     {"modelId": "52",
                                      "propertyMap": {"verificationIdentity": "", "associationKey": ""}},
                                     {"modelId": "86", "propertyMap": {"otherLoanPlatformsUnpaid": "",
                                                                       "otherLoanPlatformsInfo": "", "creditReport": "",
                                                                       "currentOverdueAmt": "", "overdueAccNum": ""}},
                                     {"modelId": "89",
                                      "propertyMap": {"businessChannelName": "", "businessChannelCode": ""}},
                                     {"modelId": "92",
                                      "propertyMap": {"appId": "", "objectId": "", "riskType": "", "riskValue": ""}},
                                     {"modelId": "93",
                                      "propertyMap": {"arbitrationInst": "", "isArbitral": "", "arbitralId": ""}},
                                     {"modelId": "26", "propertyMap": {"uumCustNo": "", "uumUserId": ""}}],
               "saleChannel": "", "instCode": "", "customerName": "",
               "phone": "", "certId": "", "marry": "", "degree": "",
               "eMail": "", "liveAddress": "",  "certType": "", "company": "", "intustry": "", "career": "", "loanPurpose": "",
               "borrowerType": "", "approveAmt": "", "approveLimit": "", "appayDate": "", "oldAppId": "",
               "customerInfo": [{"hasLoan": "", "incomeSource": "", "monthlyIncome": "", "hisLoanType": ""}],
               "lonContacts": [{"contactRelation": "", "contactName": "", "contactPhone": ""}],
               "lonAttachs": [{"attachType": "", "attachName": "", "fileId": "", "fileType": ""}],
               "tLonAccounts": [
                   {"accAccountName": "", "accAccount": "", "trusteeType": "", "accType": "", "accountType": "",
                    "accOwnIdCard": "", "accCertType": "", "accOwnPhone": "", "accCorpRep": "", "accOwnName": "",
                    "accBankCard": "", "accCity": "", "accProvince": "", "accBankBranch": "", "accBankName": "",
                    "accBankCardBindId": "", "uumCustNo": "", "extendFieldString": "", "accSubAccountNo": ""}],
               "tLonCreditReport": [{"score": "", "riskGrade": ""}],
               "loanFeeExtraInfos": [{"infoValue": "", "infoName": ""}],
               "areaList": [ {"detailAddr": "", "street": "", "district": "", "city": "", "province": "", "addrType": ""}]}"""
        date_json = json.loads(centent)
        # date_json = json.loads(SendRegisterVerificationCodejson_txt)
        print(date_json)
        print("*" * 10)
        # 发送时，每次需要注册新的手机号码，就需要json每次提示mobileTel的value进行发送
        # 遍历json文件所有的key对应的value
        dic = {}

        def json_txt(dic_json):
            if isinstance(dic_json, dict):  # 判断是否是字典类型isinstance 返回True false
                for key in dic_json:
                    if isinstance(dic_json[key], dict):  # 如果dic_json[key]依旧是字典类型
                        print("****key1--：%s value--: %s" % (key, dic_json[key]))
                        json_txt(dic_json[key])
                        dic[key] = dic_json[key]
                    elif isinstance(dic_json[key], list):
                        for dic_ in dic_json[key]:
                            print("****key2--：%s value--: %s" % (key, dic_))
                            json_txt(dic_)
                            dic[key] = dic_
                    else:
                        print("****key3--：%s value--: %s" % (key, dic_json[key]))
                        dic[key] = dic_json[key]

        json_txt(date_json)
        print("dic ---: " + str(dic))

        def  check_json_value(dic_json,k,v):
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
        check_json_value(date_json,'oldAppId','133333333331')
        check_json_value(date_json, 'accAccount', '133333333332')
        check_json_value(date_json, 'saleLicenceCode', '133333333334')
        check_json_value(date_json, 'communicateAddressCity', '133333333335')
        check_json_value(date_json, 'communicateAddressDistrict', '133333333336')
        check_json_value(date_json, 'businessChannelName', '133333333337')
        check_json_value(date_json, 'businessChannelCode', '222222222222222222')
        print("date_json 变更后   :")
        print(date_json)

if __name__ == '__main__':
    test =test()
    test.add_parameters()