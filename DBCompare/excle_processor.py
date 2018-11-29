# -*- coding: utf-8 -*-

import os
# import xlrd
from function.WPF_OperateExcel import WPF_OperateExcel
# import db_processor
import settings
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

path = os.path.dirname(os.path.abspath('.'))
file_path = settings.setting.file_path
# 配置待比较费用表名称与数据库表对应关系
config_tb = settings.setting.TABLELIST
# 存储表使用的sql语句
tb = settings.setting.SQL
# excle中sheet页名称
sheetname = settings.setting.sheetname
# 带获取数据的excle列
column = settings.setting.column

# 获取表头的指针，表头位置尽量保持该格式输入，
cursor = 0
STEP = 10
# 产品名称
productid = '475'

# 比对期数

operateExcel = WPF_OperateExcel()

# excel行数
rowCount = operateExcel.a_getExcelRowCount(file_path, sheetname)
# excel列数
columnCount = operateExcel.a_getExcelColumnCount(file_path, sheetname)

# 比较settings配置的数据信息，并且转换对应关系
def settings(title):
    if title in config_tb:
        #print('title:%s' % title)
        # print("表名称在excle中")
        tn = config_tb[title]
        if ',' in tn:
            tablename = tn.split(',')[0]
            row = tn.split(',')[1]
            sql = tb[tablename]
            return [sql, tablename, row]
        else:
            tablename = tn.split(',')[0]
            sql = tb[tablename]
            return [sql, tablename, None]
    elif title not in config_tb and title is not '' and title is not None:
        print('excel中存在的表：%s，配置中不存在对应的表名称。。。' % title)
        return False

# 取excle标表头
def excle_pro():
    cursor = 0
    title = []
    titlelist = []
    for i in range(len(column)):
        # 获取column中配置的列中的数据
        dataline = operateExcel.a_cellListReadExcel(file_path, sheetname, column[i], 1, rowCount)
        for j in range(len(dataline)):
            if cursor <= len(dataline):
                # 取表头，根据表头获取sql语句，进行数据比较
                title.append(dataline[cursor])
                tt = title[j].split('/')[0]
                titlelist.append(tt)
                cursor += STEP
    return titlelist

# 获取表内容,取表头下n行，B列的数据
# 配置中配置的行数n，'B', 'C', 'D', 'E', 'G'列的数据
# B列为6期的数据，依次类推
# title_count表头个数
def get_ExcleContent(title_count):
    # 获取标题下两行开始的数据取7行
    # column为配置的行数
    # 取表头的当前行数excle_name_col
    # 头下两行取6期所有评级的内容，取B列的内容，遇到空行为止
    #   start_ = excle_tb_name_col + 2
    #   end_ = start_ + column
    # "select * from tablename where times = column"
    contentA = []
    datalineA = []
    datalineA_child = []
    title_count = title_count+1
    time = []
    n_time = []
    for i in range(len(column)):
        # 获取column中配置的列中的数据
        dataline = operateExcel.a_cellListReadExcel(file_path, sheetname, column[i], 1, rowCount)
        datalineA.append(dataline)
        # print(dataline)
        for j in dataline:
            if ("" is j) or (None is j):
                pass
            else:
                contentA.append(j)

        # for j in range(1,title_count):
        # 这里数据重整的有问题暂时不用了
        #
        for x in range(1,3):
            times = datalineA[i][0:10]
            datalineA_child.append(times)
            time.append(times[1])

        for t in time:
            if t not in n_time:
                n_time.append(t)
    # 取期数
    ## sql中times为title下第一行数据
    return n_time,datalineA_child,datalineA

# 分别查询出所有列的sql
# 6期的sql返回结果为LEVEL_A_A,LEVEL_A,LEVEL_B_B,LEVEL_C,LEVEL_D,LEVEL_E,LEVEL_O
# 根据返回结果对比excle内容是否相等
# 将比对结果存入到excle中
#

#t = get_ExcleContent(3)
#print(t)
