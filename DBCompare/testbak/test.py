# #coding=utf-8
#
# import os
# # import xlrd
# from configparser import ConfigParser
# from WPF_OperateExcel import WPF_OperateExcel
# path = os.path.dirname(os.path.abspath('.'))
#
# operateExcel = WPF_OperateExcel()
# file_path = path + '/DBCompare/filelist/test.xlsx'
#
# #获取数据
# # data = xlrd.open_workbook(file_path)
#
# #获取sheet
# # table = data.sheet_by_name('最新定价')
#
# #获取总行数
# # nrows = table.nrows
# # print(nrows)
# #获取总列数
# # ncols = table.ncols
#
# # def excle_column():
# #     for i in range(ncols):
# #         # 获取一列的数值，例如第6列
# #         col_value = table.col_values(i)
# #
# #         for j in range(len(col_value)):
# #             list2 = []
# #             if i >= 6:
# #                 x = col_value[i]
# #                 print(x)
# #                 break
# #             else:
# #                 print(col_value[i])
# #
# #             # for j in range(len(col_value)):
# #         #
# #         #     if col_value[j] == '':
# #         #         list2.append(col_value[j])
# #         #         # 每0～9为1组
# #         #         if len(list2) == len(col_value):
# #         #             break
# #
# #
# # excle_column()
# #
# # #获取一个单元格的数值，例如第5行第6列
# # # cell_value = table.cell(1,0).value
# # # print('cell_value:----%s' % cell_value)
#
#
#
# # -*- coding: utf-8 -*-
# import os
# # from configparser import ConfigParser
# #
# # path = os.path.dirname(os.path.abspath('.'))
# # conf_path = path + '/DBCompare/config.ini'
# # config = ConfigParser()
# #
# # config.read(conf_path)
# import settings
# config_tb = settings.setting.TABLELIST
#
# def conf_name():
#     for table in config.options('TABLELIST'):
#         # print(table)
#
#         tablename = config.get('TABLELIST',table)
#         # print(tablename)
#         sqllist = config.options('SQLSCRIPT')
#         # print(sqllist)
#         if tablename in sqllist:
#             sc = config.get('SQLSCRIPT',tablename)
#
#         else:
#             pass
#     return sc
#
# conf_name()
