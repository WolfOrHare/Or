# -*- coding: utf-8 -*-
import os
class setting():
    # 待测试文件所在路径
    path = os.path.dirname(os.path.abspath('.'))
    file_path = path + '/DBCompare/filelist/test2.xlsx'
    # excle中sheet页名称
    sheetname = '最新定价'
    # 带获取数据的excle列
    column = ['A', 'B', 'C', 'D', 'E', 'G']
    # excle表头与数据库查询语句的对应关系
    # 标有名：数据库表名，取行数
    TABLELIST = {
        '信用管理费':'t_prd_product2222',
               '产品基本信息':'t_prd_product',
               '年利率':'t_prd_year_rate',
               '基础利率':'t_prd_quell_base_rate',
               '风险定价':'t_prd_risk_price',
               '期数期限':'t_prd_time_limit',
               '利率获取规则':'t_prd_rate_source',
               '额度设置':'t_prd_quota',
               '抽检信息':'t_prd_sampling_inspection',
               '保障方式 | 保障方式（担保）':'t_prd_safeguard',
               '产品开户信息配置':'t_prd_open_account_cfg',
               ' 附件':'t_prd_attachment',
               '渠道':'t_prd_channel',
               '放款资金流信息':'t_prd_relation_rule',
               '放款提现信息':'t_prd_fund_flows',
               '合同参数计算规则':'t_prd_withdraw',
               '风险备用金':'t_prd_risk_fund',
               '咨询服务费':'t_prd_consult_service_rate',
               '机构服务费':'t_prd_inst_service_rate',
               '提前结清':'t_prd_advance_settle',
               '还款设置':'t_prd_pay_set',
               '费率设置':'t_prd_fee_rate',
               '合同':'t_prd_relation_product_contract',
                '保险信息':'t_prd_isurance'
                }

    # 根据excle表内容写查询脚本，相当于指定了查询数据的列名称
    # 查询结果将于excle内容对比
    SQL = {
        't_prd_consult_service_rate':'''select LEVEL_A_A,LEVEL_A,LEVEL_B_B,LEVEL_C,LEVEL_D,LEVEL_E,LEVEL_O from t_prd_consult_service_rate where PRODUCT_ID = 298 and times = %s''',
        't_prd_product':'''select LEVEL_A_A,LEVEL_A,LEVEL_B_B,LEVEL_C,LEVEL_D,LEVEL_E,LEVEL_O from t_prd_consult_service_rate where PRODUCT_ID = 298 and times = %s''',
        't_prd_product2222':'''select LEVEL_A_A,LEVEL_A,LEVEL_B_B,LEVEL_C,LEVEL_D,LEVEL_E,LEVEL_O from t_prd_consult_service_rate where PRODUCT_ID = 298 and times = %s'''
    }

